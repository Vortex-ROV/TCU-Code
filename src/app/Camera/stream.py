from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import os
import numpy as np
import time

class CameraThread(QThread):
    frame_updated = pyqtSignal(object)

    def __init__(self):
        super(CameraThread, self).__init__()
        self.cap = cv2.VideoCapture(0)

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
                self.frame_updated.emit(rgb_image)  # Emit the frame as RGB
                self.msleep(5)
        self.cap.release() 

class Stream:
    def __init__(self, ui):
        self.ui = ui
        # self.camera_label = camera
        # self.takephoto = takephoto
        self.camera_thread = CameraThread()
        self.camera_thread.frame_updated.connect(self.update_frame)
        # self.takephoto.clicked.connect(self.save_frame)
        self.camera_thread.start()

    def update_frame(self, frame):
        h, w, ch = frame.shape
        Qframe = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(Qframe)
        self.ui.camera.setPixmap(pixmap)