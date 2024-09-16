from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import Qt

class Move(QWidget):
    def __init__(self, ui):
        super(Move, self).__init__()

        self.ui = ui

        self.movment_change_background("src/assets/images/movment.png")
        self.turn_bg_change_background("src/assets/images/turn_bg.png")
        self.turn_change_background("src/assets/images/turn.png")
        self.up_down_change_background("src/assets/images/up_down.png")
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
            self.movment_change_background("src/assets/images/right.png")
        elif right_left < 1500:
            self.movment_change_background("src/assets/images/left.png")
        if raise_descend < 1500:
            self.up_down_change_background("src/assets/images/down.png")
        elif raise_descend >1500:
            self.up_down_change_background("src/assets/images/up.png")
        else:
            self.up_down_change_background("src/assets/images/up_down.png")
        if forward_backward < 1500:
            self.movment_change_background("src/assets/images/back.png")
        elif forward_backward > 1500 :
            self.movment_change_background("src/assets/images/front.png")
        if right_left > 1500 and forward_backward < 1500:
            self.movment_change_background("src/assets/images/back_right.png")
        elif right_left < 1500 and forward_backward < 1500:
            self.movment_change_background("src/assets/images/back_left.png")
        if right_left > 1500 and forward_backward > 1500:
            self.movment_change_background("src/assets/images/front_right.png")
        elif right_left < 1500 and forward_backward > 1500:
            self.movment_change_background("src/assets/images/front_left.png")
        if right_left == 1500 and forward_backward == 1500:
            self.movment_change_background("src/assets/images/movment.png")
        if rotation > 1500:
            self.movie = QMovie("src/assets/gifs/cw.gif")
            self.movie.setScaledSize(self.turning.size())
            self.turning.setMovie(self.movie)
            self.movie.start()
        elif rotation < 1500 :
            self.movie = QMovie("src/assets/gifs/acw.gif")
            self.movie.setScaledSize(self.turning.size())
            self.turning.setMovie(self.movie)
            self.movie.start()
        else:
            self.turn_change_background("src/assets/images/turn.png")
    def movment_change_background(self, path):
        movment_pixmap = QPixmap(path)
        size = self.ui.movment.size()
        movmentscaled_pixmap = movment_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.ui.movment.setPixmap(movmentscaled_pixmap)
    def up_down_change_background(self, path):
        up_down_pixmap = QPixmap(path)
        size = self.ui.up_down.size()
        up_down_scaled_pixmap = up_down_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.ui.up_down.setPixmap(up_down_scaled_pixmap)
    def turn_change_background(self, path):
        turning_pixmap = QPixmap(path)
        size = self.ui.turning.size()
        turningscaled_pixmap = turning_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.ui.turning.setPixmap(turningscaled_pixmap)
    def turn_bg_change_background(self, path):
        turning_bg_pixmap = QPixmap(path)
        size = self.ui.turning_bg.size()
        turning_bgscaled_pixmap = turning_bg_pixmap.scaled(size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.ui.turning_bg.setPixmap(turning_bgscaled_pixmap)