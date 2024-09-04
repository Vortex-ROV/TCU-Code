from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import Qt
from Images import files
class Move(QWidget):
    def __init__(self, movment, turning_bg, turning, up_down):
        super(Move, self).__init__()
        # Movment Label
        self.movment = movment
        self.movment_change_background(":/img/movment.png")
        # Turn Label
        self.turning = turning
        self.turning_bg = turning_bg
        self.turn_change_background("turn.png")
        self.turn_bg_change_background("turn_bg.png")
        # Up Down Label
        self.up_down = up_down
        self.up_down_change_background(":/img/up_down.png")
        self.connection = False
        
    def socket_connection(self, data):
        self.connection = data
        
    def handle_joystick_logic(self, data):
        # if not self.connection:
            # return
        
        data = data.decode('utf-8')
        raise_descend =int(data[0:4])
        rotation = int(data[4:8])
        forward_backward = int(data[8:12])
        right_left = int(data[12:16])
        armed = int(data[20])
        
        # if armed == 0:
        #     return
        
        if right_left > 1500:
            self.movment_change_background(":/img/right.png")
        elif right_left < 1500:
            self.movment_change_background(":/img/left.png")
        if raise_descend < 1500:
            self.up_down_change_background(":/img/down.png")
        elif raise_descend >1500:
            self.up_down_change_background(":/img/up.png")
        else:
            self.up_down_change_background(":/img/up_down.png")
        if forward_backward < 1500:
            self.movment_change_background(":/img/back.png")
        elif forward_backward > 1500 :
            self.movment_change_background(":/img/front.png")
        if right_left > 1500 and forward_backward < 1500:
            self.movment_change_background(":/img/back_right.png")
        elif right_left < 1500 and forward_backward < 1500:
            self.movment_change_background(":/img/back_left.png")
        if right_left > 1500 and forward_backward > 1500:
            self.movment_change_background(":/img/front_right.png")
        elif right_left < 1500 and forward_backward > 1500:
            self.movment_change_background(":/img/front_left.png")
        if right_left == 1500 and forward_backward == 1500:
            self.movment_change_background(":/img/movment.png")
        if rotation > 1500:
            self.movie = QMovie("cw.gif")
            self.movie.setScaledSize(self.turning.size())  # Scale the movie to match the size of the label
            self.turning.setMovie(self.movie)
            self.movie.start()
        elif rotation < 1500 :
            self.movie = QMovie("acw.gif")
            self.movie.setScaledSize(self.turning.size())  # Scale the movie to match the size of the label
            self.turning.setMovie(self.movie)
            self.movie.start()
        else:
            self.turn_change_background("turn.png")
    def movment_change_background(self, path):
        movment_pixmap = QPixmap(path)
        size = self.movment.size()
        movmentscaled_pixmap = movment_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.movment.setPixmap(movmentscaled_pixmap)
    def up_down_change_background(self, path):
        up_down_pixmap = QPixmap(path)
        size = self.up_down.size()
        up_down_scaled_pixmap = up_down_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.up_down.setPixmap(up_down_scaled_pixmap)
    def turn_change_background(self, path):
        turning_pixmap = QPixmap(path)
        size = self.turning.size()
        turningscaled_pixmap = turning_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.turning.setPixmap(turningscaled_pixmap)
    def turn_bg_change_background(self, path):
        turning_bg_pixmap = QPixmap(path)
        size = self.turning_bg.size()
        turning_bgscaled_pixmap = turning_bg_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.turning_bg.setPixmap(turning_bgscaled_pixmap)