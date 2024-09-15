from PyQt5.QtWidgets import QWidget

class Status:
    def __init__(self, ui):

        self.ui = ui

        self.connection = False

    def socket_connection(self, data):
        self.connection = data
        print("Calledddd")

        if self.connection == True:
            self.ui.socket_status.setText(" Connected")
        elif self.connection == False:
            self.ui.socket_status.setText(" Disconnected")

    def handle_joystick_logic(self, data):
        data = data.decode('utf-8')
        lights = data[18]
        armed = int(data[21])
        joystick = int(data[-1])
        depth = int(data[-4])

        if joystick == 1:
            self.ui.joystick_status.setText(" Connected")
        elif joystick == 0:
            self.ui.joystick_status.setText(" Disconnected")
        else:
            self.ui.joystick_status.setText(" Error")

        if not self.connection:
            return

        if lights == 'H':
            self.ui.light_status.setText(" On")
        elif lights == '0':
            self.ui.light_status.setText(" Off")
        else:
            self.ui.light_status.setText(" Error")

        if armed == 1:
            if depth == 1:
                self.ui.rov_status.setText(" Depth Hold")
            else:
                self.ui.rov_status.setText(" Armed")
        elif armed == 0:
            self.ui.rov_status.setText(" Disarmed")
        else:
            self.ui.rov_status.setText(" Error")