from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLCDNumber
from PyQt5 import uic
from Camera.camera import CameraThread,Camera
from Stopwatch.stopwatch import Stopwatch
from Controls.move import Move
from Controls.grippers import Grippers
from Modes.modes import Modes
from Sensors.readings import Readings
from Status.status import Status

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("pilot.ui", self)
        # Cameras
        self.camera = self.findChild(QLabel, 'camera')
        self.takephoto = self.findChild(QPushButton, "takephoto")
        # self.fps = self.findChild(QLabel, 'fps')
        try:
            self.image = Camera(self.camera,self.takephoto)
            # self.image.start()
        except:
            print("Error in connecting to Camera")


        # Stopwatch
        self.stopwatch_screen = self.findChild(QLabel, "time_screen")
        self.time_start = self.findChild(QPushButton, "time_start")
        self.time_stop = self.findChild(QPushButton, "time_stop")
        self.time_reset = self.findChild(QPushButton, "time_reset")
        self.stopwatch = Stopwatch(self.stopwatch_screen, self.time_start, self.time_stop, self.time_reset)
        
        # Move
        self.movment = self.findChild(QLabel, "movment")
        self.turning_bg = self.findChild(QLabel, "turning_bg")
        self.turning = self.findChild(QLabel, "turning")
        self.up_down = self.findChild(QLabel, "up_down")
        self.moving = Move(self.movment, self.turning_bg, self.turning, self.up_down)

        # Grippers
        self.Gripper = self.findChild(QLabel, "gripper")
        self.rotGripper = self.findChild(QLabel, "rotGripper")
        self.gripper = Grippers(self.Gripper, self.rotGripper)        

        # Modes
        self.current_mode = self.findChild(QLabel, "current_mode")
        self.autonmous_mode = self.findChild(QLabel, "autonmous_mode")
        self.depth_hold_mode = self.findChild(QLabel, "depth_hold_mode")
        self.stabilize_mode = self.findChild(QLabel, "stabilize_mode")
        self.manual_mode = self.findChild(QLabel, "manual_mode")
        self.modes = Modes(self.current_mode, self.autonmous_mode, self.depth_hold_mode,
                            self.stabilize_mode, self.manual_mode)
        # Status
        self.rov_status = self.findChild(QLabel, "rov_status")
        self.joystick_status = self.findChild(QLabel, "joystick_status")
        self.light_status = self.findChild(QLabel, "light_status")
        self.socket_status = self.findChild(QLabel, "socket_status")
        self.status = Status(self.rov_status, self.joystick_status, self.light_status, self.socket_status)

        # Readings
        self.ROVdepth = self.findChild(QLabel, "depth")
        self.x_acc = self.findChild(QLabel, "x_acc")
        self.y_acc = self.findChild(QLabel, "y_acc")
        self.z_acc = self.findChild(QLabel, "z_acc")
        self.gyro_x = self.findChild(QLabel, "gyro_x")
        self.gyro_y = self.findChild(QLabel, "gyro_y")
        self.gyro_z = self.findChild(QLabel, "gyro_z")
        self.temp = self.findChild(QLabel, "temperature")
        self.pressure = self.findChild(QLabel, "pressure")
        self.lcd = self.findChild(QLCDNumber, "temp_lcd")
        self.readings = Readings(self.ROVdepth, self.x_acc, self.y_acc, self.z_acc, self.gyro_x, self.gyro_y, self.gyro_z, self.temp, self.pressure, self.lcd)



        self.show()