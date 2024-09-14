from .Camera.stream import Stream
# from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLCDNumber,QLineEdit,QVBoxLayout
# from PyQt5 import uic
from .Stopwatch.stopwatch import Stopwatch
from .Controls.move import Move
from .Controls.grippers import Grippers
from .Modes.modes import Modes
from .Sensors.readings import Readings
from .Sensors.compass import CompassWidget
from .Status.status import Status

class Backend():
    def __init__(self):
        # super(UI, self).__init__()
        pass

    def setupUi(self, ui):
        self.image = Stream(ui)
        self.stopwatch = Stopwatch(ui)
        self.moving = Move(ui)
        self.grippers = Grippers(ui)
        self.modes = Modes(ui)
        self.readings = Readings(ui)
        self.compass = CompassWidget(ui)
        self.status = Status(ui)