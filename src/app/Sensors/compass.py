import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QPainterPath, QBrush, QColor
from PyQt5.QtCore import Qt, QPointF

import math

class CompassWidget(QWidget):
    def __init__(self, ui):
        super().__init__()

        self.setWindowTitle('Compass Widget')
        self.setGeometry(100, 100, 100, 100)

        self.angle = 0

    def update_angle(self, angle):
        self.angle = angle
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        side = min(self.width(), self.height())
        painter.setViewport((self.width() - side) // 2, (self.height() - side) // 2, side, side)
        painter.setWindow(-50, -50, 100, 100)

        painter.setPen(Qt.white)
        painter.setBrush(QColor("#212121"))
        painter.drawEllipse(-48, -48, 96, 96)

        for i in range(0, 360, 1):
            painter.setPen(QPen(Qt.white, 0.5))

            if i % 45 == 0:
                painter.drawLine(
                    QPointF(48 * math.cos(i * math.pi / 180), 48 * math.sin(i * math.pi / 180)),
                    QPointF(40 * math.cos(i * math.pi / 180), 40 * math.sin(i * math.pi / 180))
                )
            else:
                painter.drawLine(
                    QPointF(48 * math.cos(i * math.pi / 180), 48 * math.sin(i * math.pi / 180)),
                    QPointF(45 * math.cos(i * math.pi / 180), 45 * math.sin(i * math.pi / 180))
                )
                
        path = QPainterPath()

        painter.rotate(self.angle)
        painter.translate(0, 5)
        path.moveTo(0, 0)
        path.lineTo(-5, -5)
        path.lineTo(0, -40)
        path.lineTo(5, -5)
        path.lineTo(0, 0)
        painter.fillPath(path, QBrush(QColor("#fd8a44")))

        path.moveTo(0, 0)
        path.lineTo(-5, -5)
        path.lineTo(0, -40)
        path.lineTo(5, -5)
        path.lineTo(0, 0)
        painter.strokePath(path, QPen(Qt.white, 1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    compass = CompassWidget()
    compass.show()
    sys.exit(app.exec_())
