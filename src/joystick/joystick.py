import json
import pygame
from PyQt5.QtCore import QThread, pyqtSignal
import time
from .auto_transplanting import AutoTransplanting
from .joystick_mapper import JoystickMapper

class JoyStick(QThread):
    signal = pyqtSignal(bytes)
    def __init__(self):
        super().__init__()

        pygame.init()
        pygame.joystick.init()

        self.__joystick = None
        self.__joystick_name = None
        self.__configs = {}

        self.__new_values = [0, 0, 0, 0, 0, 0, 0, 'O', 0, 0, 'M', 0]
        self.__old_values = [0, 0, 0, 0, 0, 0, 0, 'O', 0, 0, 'M', 0]
        self.__old__button_input = []

        self.auto_transplanting = AutoTransplanting(1)
    
    def __is_pressed(self,butt_num):
        return self.__old__button_input[butt_num] != self.__joystick.get_button(butt_num) and self.__joystick.get_button(butt_num)
    
    def __updated_old_button_input_list(self,num_list):
        for val in num_list:
            self.__old__button_input[val] = self.__joystick.get_button(val)
            
    def __handle_input(self):
        # throttle (up, down), yaw, forward/backwards, lateral (left, right), gripper 1, gripper 2, light, rotating gripper (0: off / left / right), arm/disarm, flight mode, joystick connection
        
        self.__new_values = [
            -self.__joystick.get_axis(self.__configs["throttle"]),
            (self.__joystick.get_axis(self.__configs["yaw_r"]) / 2 + 0.5) - (self.__joystick.get_axis(self.__configs["yaw_l"]) / 2 + 0.5),
            -self.__joystick.get_axis(self.__configs["forwardBackward"]),
            self.__joystick.get_axis(self.__configs["lateral"]),
            
            int(not self.__old_values[4] if self.__is_pressed(self.__configs["gripper1"]) else self.__old_values[4]),
            int(not self.__old_values[5] if self.__is_pressed(self.__configs["gripper2"]) else self.__old_values[5]),

            # placeholder for light
            # int(not0 self.__old_values[6] if self.__is_pressed(self.__configs["light"]) else self.__old_values[6]),
            self.__old_values[6],

            # placeholder for rotating gripper
            self.__old_values[7],
            
            int(not self.__old_values[8] if self.__is_pressed(self.__configs["arm_rotating_gripper"]) else self.__old_values[8]),

            # placeholder for arm/disarm
            self.__old_values[9],

            # placeholder for flight mode
            self.__old_values[10],

            # placeholder for joystick connection
            self.__old_values[11]
        ]

        if self.__new_values[6] == 0 and self.__is_pressed(self.__configs["light"]):
            self.__new_values[6] = 'H'
        elif self.__new_values[6] == 'H' and self.__is_pressed(self.__configs["light"]):
            self.__new_values[6] = 0
 
        # rotating gripper
        if self.__new_values[8] == 1 and self.__joystick.get_button(self.__configs["rotatingGripperLeft"]) and not self.__joystick.get_button(self.__configs["rotatingGripperRight"]):
            self.__new_values[7] = 'L'
        elif self.__new_values[8] == 1 and self.__joystick.get_button(self.__configs["rotatingGripperRight"]) and not self.__joystick.get_button(self.__configs["rotatingGripperLeft"]):
            self.__new_values[7] = 'R'
        else:
            self.__new_values[7] = 'O'

        # arm/disarm
        if self.__old_values[9] == 0 and self.__joystick.get_button(self.__configs["arm"]):
            self.__new_values[9] = 1
        if self.__old_values[9] == 1 and self.__joystick.get_button(self.__configs["disarm"]):
            self.__new_values[9] = 0

        # flight mode
        if(self.__joystick_name == "Xbox 360 Controller" or self.__joystick_name == "Controller (Xbox One For Windows)"):
            if self.__joystick.get_hat(0)[0] == 1:
                self.__new_values[10] = 'S'
            elif self.__joystick.get_hat(0)[0] == -1:
                self.__new_values[10] = 'A'
            elif self.__joystick.get_hat(0)[1] == 1:
                self.__new_values[10] = 'M'
            # elif self.__joystick.get_hat(0)[1] == -1:
                # self.__new_values[10] = 'D'
        elif self.__joystick_name == "DualSense Wireless Controller" or self.__joystick_name == "PS4 Controller":
            if self.__joystick.get_button(11):
                self.__new_values[10] = 'S'
            elif self.__joystick.get_button(12):
                self.__new_values[10] = 'A'
            elif self.__joystick.get_button(13):
                self.__new_values[10] = 'M'
            # elif self.__joystick.get_button(14):
                # self.__new_values[10] = 'W'

        if self.__new_values[8] == 1:
            self.__new_values[10] = 'A'
            self.__new_values[0] = 0
            self.__new_values[1] = 0
            self.__new_values[2] = 0
            self.__new_values[3] = 0
                
        self.auto_transplanting.do_plan(self.__new_values,self.signal)
        if self.auto_transplanting.autonomus_plan == 1:
            if self.auto_transplanting.autonomus != 2:
                self.send_values()
        elif self.auto_transplanting.autonomus_plan == 2:
            if self.auto_transplanting.autonomus == 0:
                self.send_values()
                                    
        if (self.__is_pressed(self.__configs["auto"])):
            self.auto_transplanting.increament()

        self.__updated_old_button_input_list([self.__configs["auto"]])
        
        
        if self.__is_pressed(6):
            print("saved pressure at prop")
            self.auto_transplanting.pressure_at_prop = 100

        if self.__is_pressed(7):
            print("saved pressure above prop")
            self.auto_transplanting.pressure_above_prop = 200

        self.__updated_old_button_input_list([self.__configs["gripper1"], self.__configs["light"], self.__configs["gripper2"], self.__configs["arm_rotating_gripper"], self.__configs["auto"]])

    def get_pressure(self,data):
        
        if(len(self.__old__button_input) and self.__joystick is not None):
            if self.__is_pressed(6):
                print("saved pressure at prop")
                self.auto_transplanting.pressure_at_prop = float(data[36:42])

            if self.__is_pressed(7):
                print("saved pressure above prop")
                self.auto_transplanting.pressure_above_prop = float(data[36:42])

            self.auto_transplanting.current_pressure = float(data[36:42])
            self.__updated_old_button_input_list([6,7])
        
            
    def send_values(self):
        
        gui_commands = str(JoystickMapper.map(self.__new_values))
        if self.__new_values == self.__old_values:
            return 
  
        self.__old_values = self.__new_values.copy()
        self.signal.emit(gui_commands[1:len(gui_commands)-1].replace(", ","").replace("'", "").encode())
        time.sleep(0.01)
      
                
    def __handle_joystick_disconnect(self):
        if pygame.joystick.get_count() > 0 and self.__joystick is not None:
            return
        
        while pygame.joystick.get_count() == 0:
            self.__new_values = [1500, 1500, 1500, 1500, 0, 0, 0, 'O', 0, 0, 'M', 0]
            if self.__new_values != self.__old_values:
                gui_commands = str(self.__new_values)
                self.signal.emit(gui_commands[1:len(gui_commands)-1].replace(", ","").replace("'", "").encode())
                self.__old_values = self.__new_values.copy()

            print('No joystick connected')
            pygame.time.wait(200)
        
        self.__new_values = [1500, 1500, 1500, 1500, 0, 0, 0, 'O', 0, 0, 'M', 1]
        gui_commands = str(self.__new_values)
        self.signal.emit(gui_commands[1:len(gui_commands)-1].replace(", ","").replace("'", "").encode())
        self.__old_values = self.__new_values.copy()
        
        print('joystick connected succesfully')
        self.__joystick = pygame.joystick.Joystick(0)
        self.__joystick.init()
        
        self.__joystick_name = self.__joystick.get_name()
        print("Joystick Name:", self.__joystick_name)
        
        self.__load_joystick_configurations("joystick/configurations.json")
        self.__old__button_input = [0 for _ in range (self.__configs["buttons_cnt"])]
        print(self.__old__button_input)
    
    
    def connect_signal(self, slot):
        self.signal.connect(slot)
        
    def __load_joystick_configurations(self, json_path):
        data = {}
        try:
            with open(json_path) as f:
                data = json.load(f)
            f.close()
        except FileNotFoundError:
            print("File not found. Please provide a valid file path.")
        
        self.__configs = data[self.__joystick_name]
                   
    def run(self):
        clock = pygame.time.Clock()
        fps = 60

        while True:
            self.__handle_joystick_disconnect()
            pygame.event.pump()
            self.__handle_input()
            clock.tick(fps)


# joystick = JoyStick()
# joystick.connect_signal(print)
# joystick.run()
