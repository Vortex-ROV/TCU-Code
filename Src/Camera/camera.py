from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, pyqtSignal
import cv2
from vidgear.gears import NetGear
import sys
import os
import numpy as np

class CameraThread(QThread):
    frame_updated = pyqtSignal(object)
    camera_No =0
    def __init__(self, address = "192.168.33.100", port = "5454"):
        super(CameraThread, self).__init__()
        options={
            "max_retries":sys.maxsize
        }
        self.client = NetGear(
            address = address,
            port = port,
            protocol = "tcp",
            pattern = 0,
            receive_mode = True,
            logging = True,
            **options
        )
    def run(self):
        if self.camera_No == 1 :
            i=0
            while True:
                # #Camera blue robotics   
                frame = self.client.recv()
                print(frame.shape)
                i+=1
                if frame is not None:
                    # rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    # rotated_frame = cv2.rotate(frame, cv2.ROTATE_180)
                    # cv2.imshow("Hello",rotated_frame)
                    
                    key = cv2.waitKey(1) 
                    if key == ord(' '):
                        frame_filename = os.path.join("D:/frames", "frame_{}.jpg".format(len(os.listdir("D:/frames"))))
                        print(len(os.listdir("D:/frames")))
                        cv2.imwrite(frame_filename, frame)
                        # cv2.imwrite(f"frame {i}",rotated_frame)
                    # Convert BGR to RGB
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    cv2.imshow("3D Model Frames",frame)
                    self.frame_updated.emit(rgb_image)
                    
               

        else :   
            #Camera hendi 
            i=0
            while True:
                frame = self.client.recv()
                i+=1
                if frame is not None:
                    # rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    rotated_frame = cv2.rotate(frame, cv2.ROTATE_180)
                    # cv2.imshow("Hello",rotated_frame)
                    
                    
                    key = cv2.waitKey(1) 
                    if key == ord(' '):
                        frame_filename = os.path.join("D:/frames", "frame_{}.jpg".format(len(os.listdir("D:/frames"))))
                        print(len(os.listdir("D:/frames")))
                        cv2.imwrite(frame_filename, rotated_frame)
                        # cv2.imwrite(f"frame {i}",rotated_frame)
                    # Convert BGR to RGB
                    rgb_image = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2RGB)
                    cv2.imshow("555555",rotated_frame)
                    self.frame_updated.emit(rgb_image)

class Camera:
    def __init__(self, camera,takephoto):
        self.camera_label = camera
        self.photo=takephoto
        # self.setCentralWidget(self.camera_label)
        self.camera_thread = CameraThread(address="192.168.33.100")
        self.camera_thread.frame_updated.connect(self.update_frame)
        self.photo.clicked.connect(self.save_frame)
        self.camera_thread.start()

    def update_frame(self, frame):
        h, w, ch = frame.shape
        Qframe = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(Qframe)
        self.camera_label.setPixmap(pixmap)
    
    def save_frame(self):
        # Get the frame currently displayed on the GUI
        pixmap = self.camera_label.pixmap()
        if pixmap is not None:
            frame = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
            frame_data = frame.constBits()
            frame_data.setsize(frame.byteCount())
            frame_array = np.array(frame_data).reshape(frame.height(), frame.width(), 3)
            # Create a directory if it doesn't exist
            os.makedirs("frames", exist_ok=True)
            # Save the frame
            frame_filename = os.path.join("frames", "frame_{}.jpg".format(len(os.listdir("frames"))))
            cv2.imwrite(frame_filename, cv2.cvtColor(frame_array, cv2.COLOR_RGB2BGR))
            print("Frame saved:", frame_filename)
    