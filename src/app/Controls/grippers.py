from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import Qt

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
        
        data = data.decode('utf-8')

        first_gripper = int(data[16])
        sec_gripper = int(data[17])
        gripper_rotation = data[19]
        armed = int(data[21])
        
        # if armed == 0:
        #     return

        if first_gripper == 1:
            self.gripper_background("src/assets/images/gripperOpen.png")
            # self.gripper_background("src/assets/images/gripperOpen.png")
        else:
            self.gripper_background("src/assets/images/gripperClose.png")
            #self.label_raise.setStyleSheet("image:url(:/icons/raisearrow.svg);")
        # if sec_gripper == 1:
        #     self.rotGripper_background(":/img/rotGripper_open.png")
        # else:
        #     self.rotGripper_background(":/img/rotGripper_close.png")
        if gripper_rotation == "O":
            if sec_gripper == 1:
                self.rotGripper_background("src/assets/images/rotGripperOpen.png")
            elif sec_gripper == 0:
                self.rotGripper_background("src/assets/images/rotGripperClose.png")
        elif gripper_rotation == "L":
            if sec_gripper == 1:
                # self.movie = QMovie("rot_gripper_open_cw.gif")
                self.movie = QMovie("src/assets/gifs/rotGripperOpenCW.gif")
                self.movie.setScaledSize(self.rotGripper.size())
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
            elif sec_gripper == 0:
                self.movie = QMovie("src/assets/gifs/rotGripperCloseCW.gif")
                self.movie.setScaledSize(self.rotGripper.size())
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
        elif gripper_rotation == "R":
            if sec_gripper == 1:
                self.movie = QMovie("src/assets/gifs/rotGripperOpenCCW.gif")
                self.movie.setScaledSize(self.rotGripper.size())
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
            elif sec_gripper == 0:
                self.movie = QMovie("src/assets/gifs/rotGripperCloseCCW.gif")
                self.movie.setScaledSize(self.rotGripper.size())
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
        

    def gripper_background(self, path):
        gripper_pixmap = QPixmap(path)
        size = self.ui.gripper.size()
        gripperscaled_pixmap = gripper_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.ui.gripper.setPixmap(gripperscaled_pixmap)

    def rotGripper_background(self, path):
        rotGripper_pixmap = QPixmap(path)
        size = self.ui.rotGripper.size()
        rotGripperscaled_pixmap = rotGripper_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.ui.rotGripper.setPixmap(rotGripperscaled_pixmap)