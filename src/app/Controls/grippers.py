from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMovie
from communication.message import Message


class Grippers:
    def __init__(self, ui):
        super(Grippers, self).__init__()

        self.ui = ui

        self.gripper_background("src/assets/images/gripperClose.png")
        self.rotGripper_background("src/assets/images/rotGripperClose.png")

        self.connection = False

    def socket_connection(self, data):
        self.connection = data

    def handle_joystick_logic(self, data):
        # if not self.connection:
        #     return

        data = Message(data)

        first_gripper = data.get_value("gripper_1")
        sec_gripper = data.get_value("gripper_2")
        gripper_rotation = data.get_value("rotating_gripper")
        armed = data.get_value("armed")

        # if armed:
        #     return

        if first_gripper == True:
            self.gripper_background("src/assets/images/gripperOpen.png")
        else:
            self.gripper_background("src/assets/images/gripperClose.png")
        if gripper_rotation == "O":
            if sec_gripper == True:
                self.rotGripper_background("src/assets/images/rotGripperOpen.png")
            elif sec_gripper == False:
                self.rotGripper_background("src/assets/images/rotGripperClose.png")
        elif gripper_rotation == "L":
            if sec_gripper == True:
                self.movie = QMovie("src/assets/gifs/rotGripperOpenCW.gif")
                self.movie.setScaledSize(self.rotGripper.size())
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
            elif sec_gripper == False:
                self.movie = QMovie("src/assets/gifs/rotGripperCloseCW.gif")
                self.movie.setScaledSize(self.rotGripper.size())
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
        elif gripper_rotation == "R":
            if sec_gripper == True:
                self.movie = QMovie("src/assets/gifs/rotGripperOpenCCW.gif")
                self.movie.setScaledSize(self.rotGripper.size())
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
            elif sec_gripper == False:
                self.movie = QMovie("src/assets/gifs/rotGripperCloseCCW.gif")
                self.movie.setScaledSize(self.rotGripper.size())
                self.rotGripper.setMovie(self.movie)
                self.movie.start()

    def gripper_background(self, path):
        gripper_pixmap = QPixmap(path)
        size = self.ui.gripper.size()
        gripperscaled_pixmap = gripper_pixmap.scaled(
            size,
            aspectRatioMode=Qt.KeepAspectRatio,
            transformMode=Qt.SmoothTransformation,
        )
        self.ui.gripper.setPixmap(gripperscaled_pixmap)

    def rotGripper_background(self, path):
        rotGripper_pixmap = QPixmap(path)
        size = self.ui.rotGripper.size()
        rotGripperscaled_pixmap = rotGripper_pixmap.scaled(
            size,
            aspectRatioMode=Qt.KeepAspectRatio,
            transformMode=Qt.SmoothTransformation,
        )
        self.ui.rotGripper.setPixmap(rotGripperscaled_pixmap)
