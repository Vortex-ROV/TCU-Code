from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import Qt
from Images import files

class Grippers:
    def __init__(self, gripper, rotGripper):
        # super(Grippers, self).__init__()

        # Front Gripper
        self.gripper = gripper
        self.gripper_background(":/img/gripper_close.png")

        # Side Gripper
        self.rotGripper = rotGripper
        self.rotGripper_background(":/img/rotGripper_close.png")

        self.connection = False

    def socket_connection(self, data):
        self.connection = data

    def handle_joystick_logic(self, data):
        pass
        # if not self.connection:
        #     return
        
        """
        data = data.decode('utf-8')

        first_gripper = int(data[16])
        sec_gripper = int(data[17])
        gripper_rotation = data[19]
        armed = int(data[21])
        
        # if armed == 0:
        #     return

        if first_gripper == 1:
            self.gripper_background(":/img/gripper_open.png")
        else:
            self.gripper_background(":/img/gripper_close.png")
            #self.label_raise.setStyleSheet("image:url(:/icons/raisearrow.svg);")
        # if sec_gripper == 1:
        #     self.rotGripper_background(":/img/rotGripper_open.png")
        # else:
        #     self.rotGripper_background(":/img/rotGripper_close.png")
        if gripper_rotation == "O":
            if sec_gripper == 1:
                self.rotGripper_background(":/img/rot_gripper_open.png")
            elif sec_gripper == 0:
                self.rotGripper_background(":/img/rot_gripper_close.png")
        elif gripper_rotation == "L":
            if sec_gripper == 1:
                self.movie = QMovie("rot_gripper_open_cw.gif")
                self.movie.setScaledSize(self.rotGripper.size())  # Scale the movie to match the size of the label
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
            elif sec_gripper == 0:
                self.movie = QMovie("rot_gripper_close_cw.gif")
                self.movie.setScaledSize(self.rotGripper.size())  # Scale the movie to match the size of the label
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
        elif gripper_rotation == "R":
            if sec_gripper == 1:
                self.movie = QMovie("rot_gripper_open_ccw.gif")
                self.movie.setScaledSize(self.rotGripper.size())  # Scale the movie to match the size of the label
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
            elif sec_gripper == 0:
                self.movie = QMovie("rot_gripper_close_ccw.gif")
                self.movie.setScaledSize(self.rotGripper.size())  # Scale the movie to match the size of the label
                self.rotGripper.setMovie(self.movie)
                self.movie.start()
        """
        

    def gripper_background(self, path):
        gripper_pixmap = QPixmap(path)
        size = self.gripper.size()
        gripperscaled_pixmap = gripper_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.gripper.setPixmap(gripperscaled_pixmap)

    def rotGripper_background(self, path):
        rotGripper_pixmap = QPixmap(path)
        size = self.rotGripper.size()
        rotGripperscaled_pixmap = rotGripper_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.rotGripper.setPixmap(rotGripperscaled_pixmap)