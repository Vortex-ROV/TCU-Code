# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilot.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VortexGUI(object):
    def setupUi(self, VortexGUI):
        VortexGUI.setObjectName("VortexGUI")
        VortexGUI.resize(1908, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VortexGUI.sizePolicy().hasHeightForWidth())
        VortexGUI.setSizePolicy(sizePolicy)
        VortexGUI.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        VortexGUI.setFocusPolicy(QtCore.Qt.StrongFocus)
        VortexGUI.setWindowOpacity(1.0)
        VortexGUI.setStyleSheet("background-color: #171717;")
        self.centralwidget = QtWidgets.QWidget(VortexGUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.current_mode = QtWidgets.QLabel(self.centralwidget)
        self.current_mode.setGeometry(QtCore.QRect(1178, 785, 361, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_mode.sizePolicy().hasHeightForWidth())
        self.current_mode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.current_mode.setFont(font)
        self.current_mode.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.current_mode.setObjectName("current_mode")
        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(20, 70, 1530, 670))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera.sizePolicy().hasHeightForWidth())
        self.camera.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.camera.setFont(font)
        self.camera.setStyleSheet("background-color: transparent;\n"
"border-radius: 5px;\n"
"")
        self.camera.setText("")
        self.camera.setScaledContents(True)
        self.camera.setAlignment(QtCore.Qt.AlignCenter)
        self.camera.setObjectName("camera")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 940, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("background-color: #212121;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.title.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 765, 1551, 220))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #212121;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.realTimeViewFrame = QtWidgets.QFrame(self.centralwidget)
        self.realTimeViewFrame.setGeometry(QtCore.QRect(1570, 330, 340, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realTimeViewFrame.sizePolicy().hasHeightForWidth())
        self.realTimeViewFrame.setSizePolicy(sizePolicy)
        self.realTimeViewFrame.setStyleSheet("background-color: #212121;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.realTimeViewFrame.setProperty("text", "")
        self.realTimeViewFrame.setObjectName("realTimeViewFrame")
        self.compass_label = QtWidgets.QLabel(self.realTimeViewFrame)
        self.compass_label.setGeometry(QtCore.QRect(100, 250, 135, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compass_label.sizePolicy().hasHeightForWidth())
        self.compass_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.compass_label.setFont(font)
        self.compass_label.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.compass_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.compass_label.setLineWidth(2)
        self.compass_label.setObjectName("compass_label")
        self.pressure = QtWidgets.QLabel(self.realTimeViewFrame)
        self.pressure.setGeometry(QtCore.QRect(14, 60, 161, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure.sizePolicy().hasHeightForWidth())
        self.pressure.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pressure.setFont(font)
        self.pressure.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.pressure.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pressure.setLineWidth(1)
        self.pressure.setObjectName("pressure")
        self.depth = QtWidgets.QLabel(self.realTimeViewFrame)
        self.depth.setGeometry(QtCore.QRect(181, 60, 155, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.depth.sizePolicy().hasHeightForWidth())
        self.depth.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.depth.setFont(font)
        self.depth.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.depth.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.depth.setLineWidth(2)
        self.depth.setObjectName("depth")
        self.rov_name_2 = QtWidgets.QLabel(self.realTimeViewFrame)
        self.rov_name_2.setGeometry(QtCore.QRect(14, 13, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rov_name_2.sizePolicy().hasHeightForWidth())
        self.rov_name_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rov_name_2.setFont(font)
        self.rov_name_2.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"")
        self.rov_name_2.setLineWidth(2)
        self.rov_name_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rov_name_2.setObjectName("rov_name_2")
        self.compass = QtWidgets.QLabel(self.realTimeViewFrame)
        self.compass.setGeometry(QtCore.QRect(100, 110, 135, 135))
        self.compass.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.compass.setText("")
        self.compass.setAlignment(QtCore.Qt.AlignCenter)
        self.compass.setObjectName("compass")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 775, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.up_down = QtWidgets.QLabel(self.centralwidget)
        self.up_down.setGeometry(QtCore.QRect(190, 815, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up_down.sizePolicy().hasHeightForWidth())
        self.up_down.setSizePolicy(sizePolicy)
        self.up_down.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.up_down.setText("")
        self.up_down.setAlignment(QtCore.Qt.AlignCenter)
        self.up_down.setObjectName("up_down")
        self.gripper = QtWidgets.QLabel(self.centralwidget)
        self.gripper.setGeometry(QtCore.QRect(760, 815, 230, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gripper.sizePolicy().hasHeightForWidth())
        self.gripper.setSizePolicy(sizePolicy)
        self.gripper.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: white;\n"
"border-radius: 5px;")
        self.gripper.setText("")
        self.gripper.setAlignment(QtCore.Qt.AlignCenter)
        self.gripper.setObjectName("gripper")
        self.rotGripper = QtWidgets.QLabel(self.centralwidget)
        self.rotGripper.setGeometry(QtCore.QRect(520, 815, 230, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotGripper.sizePolicy().hasHeightForWidth())
        self.rotGripper.setSizePolicy(sizePolicy)
        self.rotGripper.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: white;\n"
"border-radius: 5px;")
        self.rotGripper.setText("")
        self.rotGripper.setAlignment(QtCore.Qt.AlignCenter)
        self.rotGripper.setObjectName("rotGripper")
        self.movment = QtWidgets.QLabel(self.centralwidget)
        self.movment.setGeometry(QtCore.QRect(30, 815, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movment.sizePolicy().hasHeightForWidth())
        self.movment.setSizePolicy(sizePolicy)
        self.movment.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.movment.setText("")
        self.movment.setAlignment(QtCore.Qt.AlignCenter)
        self.movment.setObjectName("movment")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 775, 101, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.title_2 = QtWidgets.QLabel(self.centralwidget)
        self.title_2.setGeometry(QtCore.QRect(920, 10, 990, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setStyleSheet("background-color: #212121;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.title_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.title_2.setObjectName("title_2")
        self.turning_bg = QtWidgets.QLabel(self.centralwidget)
        self.turning_bg.setGeometry(QtCore.QRect(350, 815, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turning_bg.sizePolicy().hasHeightForWidth())
        self.turning_bg.setSizePolicy(sizePolicy)
        self.turning_bg.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.turning_bg.setText("")
        self.turning_bg.setAlignment(QtCore.Qt.AlignCenter)
        self.turning_bg.setObjectName("turning_bg")
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1920, 991))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_label.sizePolicy().hasHeightForWidth())
        self.background_label.setSizePolicy(sizePolicy)
        self.background_label.setStyleSheet("background-color: #171717;")
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.rempFrame = QtWidgets.QFrame(self.centralwidget)
        self.rempFrame.setGeometry(QtCore.QRect(1570, 640, 341, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rempFrame.sizePolicy().hasHeightForWidth())
        self.rempFrame.setSizePolicy(sizePolicy)
        self.rempFrame.setStyleSheet("background-color: #212121;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.rempFrame.setProperty("text", "")
        self.rempFrame.setObjectName("rempFrame")
        self.temp_lcd = QtWidgets.QLCDNumber(self.rempFrame)
        self.temp_lcd.setGeometry(QtCore.QRect(10, 63, 321, 71))
        self.temp_lcd.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 5px;")
        self.temp_lcd.setObjectName("temp_lcd")
        self.offset_button = QtWidgets.QPushButton(self.rempFrame)
        self.offset_button.setGeometry(QtCore.QRect(176, 10, 48, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.offset_button.setFont(font)
        self.offset_button.setStyleSheet("QPushButton{\n"
"background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #fd8a44; \n"
"    border-color: #fd8a44; \n"
"}")
        self.offset_button.setObjectName("offset_button")
        self.temperature = QtWidgets.QLabel(self.rempFrame)
        self.temperature.setGeometry(QtCore.QRect(10, 10, 160, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperature.sizePolicy().hasHeightForWidth())
        self.temperature.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.temperature.setFont(font)
        self.temperature.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.temperature.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.temperature.setLineWidth(2)
        self.temperature.setObjectName("temperature")
        self.offset_input = QtWidgets.QLineEdit(self.rempFrame)
        self.offset_input.setGeometry(QtCore.QRect(232, 10, 101, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.offset_input.setFont(font)
        self.offset_input.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.offset_input.setText("")
        self.offset_input.setObjectName("offset_input")
        self.rovStatusFrame = QtWidgets.QFrame(self.centralwidget)
        self.rovStatusFrame.setGeometry(QtCore.QRect(1570, 60, 340, 260))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rovStatusFrame.sizePolicy().hasHeightForWidth())
        self.rovStatusFrame.setSizePolicy(sizePolicy)
        self.rovStatusFrame.setStyleSheet("background-color: #212121;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.rovStatusFrame.setProperty("text", "")
        self.rovStatusFrame.setObjectName("rovStatusFrame")
        self.rov_status = QtWidgets.QLabel(self.rovStatusFrame)
        self.rov_status.setGeometry(QtCore.QRect(10, 200, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rov_status.setFont(font)
        self.rov_status.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-top: white 3px solid;\n"
"border-radius: 5px;")
        self.rov_status.setText("")
        self.rov_status.setObjectName("rov_status")
        self.joystick_status = QtWidgets.QLabel(self.rovStatusFrame)
        self.joystick_status.setGeometry(QtCore.QRect(169, 120, 161, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.joystick_status.setFont(font)
        self.joystick_status.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-top: white 3px solid;\n"
"border-radius: 5px;")
        self.joystick_status.setText("")
        self.joystick_status.setObjectName("joystick_status")
        self.label_14 = QtWidgets.QLabel(self.rovStatusFrame)
        self.label_14.setGeometry(QtCore.QRect(170, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"")
        self.label_14.setObjectName("label_14")
        self.light_status = QtWidgets.QLabel(self.rovStatusFrame)
        self.light_status.setGeometry(QtCore.QRect(169, 200, 161, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.light_status.setFont(font)
        self.light_status.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-top: white 3px solid;\n"
"border-radius: 5px;")
        self.light_status.setText("")
        self.light_status.setObjectName("light_status")
        self.label_9 = QtWidgets.QLabel(self.rovStatusFrame)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.socket_status = QtWidgets.QLabel(self.rovStatusFrame)
        self.socket_status.setGeometry(QtCore.QRect(10, 120, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.socket_status.setFont(font)
        self.socket_status.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-top: white 3px solid;\n"
"border-radius: 5px;")
        self.socket_status.setText("")
        self.socket_status.setObjectName("socket_status")
        self.rov_name = QtWidgets.QLabel(self.rovStatusFrame)
        self.rov_name.setGeometry(QtCore.QRect(10, 0, 171, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rov_name.sizePolicy().hasHeightForWidth())
        self.rov_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rov_name.setFont(font)
        self.rov_name.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"")
        self.rov_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rov_name.setObjectName("rov_name")
        self.label_8 = QtWidgets.QLabel(self.rovStatusFrame)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.rovStatusFrame)
        self.label_12.setGeometry(QtCore.QRect(170, 170, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.rovStatusFrame)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(30, 160, 101, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: transparent;\n"
"color: white;")
        self.label_19.setObjectName("label_19")
        self.fps = QtWidgets.QLabel(self.centralwidget)
        self.fps.setGeometry(QtCore.QRect(44, 160, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fps.setFont(font)
        self.fps.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.fps.setObjectName("fps")
        self.manual_mode = QtWidgets.QLabel(self.centralwidget)
        self.manual_mode.setGeometry(QtCore.QRect(1281, 841, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.manual_mode.setFont(font)
        self.manual_mode.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.manual_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.manual_mode.setObjectName("manual_mode")
        self.autonmous_mode = QtWidgets.QLabel(self.centralwidget)
        self.autonmous_mode.setGeometry(QtCore.QRect(1281, 937, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.autonmous_mode.setFont(font)
        self.autonmous_mode.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.autonmous_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.autonmous_mode.setObjectName("autonmous_mode")
        self.stabilize_mode = QtWidgets.QLabel(self.centralwidget)
        self.stabilize_mode.setGeometry(QtCore.QRect(1377, 889, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stabilize_mode.setFont(font)
        self.stabilize_mode.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.stabilize_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.stabilize_mode.setObjectName("stabilize_mode")
        self.depth_hold_mode = QtWidgets.QLabel(self.centralwidget)
        self.depth_hold_mode.setGeometry(QtCore.QRect(1178, 889, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.depth_hold_mode.setFont(font)
        self.depth_hold_mode.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.depth_hold_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.depth_hold_mode.setObjectName("depth_hold_mode")
        self.turning = QtWidgets.QLabel(self.centralwidget)
        self.turning.setGeometry(QtCore.QRect(350, 815, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turning.sizePolicy().hasHeightForWidth())
        self.turning.setSizePolicy(sizePolicy)
        self.turning.setStyleSheet("background-color:transparent;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.turning.setText("")
        self.turning.setAlignment(QtCore.Qt.AlignCenter)
        self.turning.setObjectName("turning")
        self.takephoto = QtWidgets.QPushButton(self.centralwidget)
        self.takephoto.setGeometry(QtCore.QRect(1010, 815, 141, 150))
        self.takephoto.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.takephoto.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Vortex/MATE 2024/Pilot/Images/3d-modeling.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.takephoto.setIcon(icon)
        self.takephoto.setIconSize(QtCore.QSize(50, 50))
        self.takephoto.setObjectName("takephoto")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1030, 780, 101, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: transparent;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.camera_frame = QtWidgets.QFrame(self.centralwidget)
        self.camera_frame.setGeometry(QtCore.QRect(10, 60, 1550, 690))
        self.camera_frame.setStyleSheet("background-color: #212121;\n"
"color: white;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.camera_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera_frame.setObjectName("camera_frame")
        self.watchFrame = QtWidgets.QFrame(self.centralwidget)
        self.watchFrame.setGeometry(QtCore.QRect(1570, 804, 340, 181))
        self.watchFrame.setStyleSheet("background-color: #212121;\n"
"color: white;\n"
"border-radius: 5px;\n"
"")
        self.watchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.watchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.watchFrame.setObjectName("watchFrame")
        self.time_reset = QtWidgets.QPushButton(self.watchFrame)
        self.time_reset.setGeometry(QtCore.QRect(90, 120, 161, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_reset.sizePolicy().hasHeightForWidth())
        self.time_reset.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time_reset.setFont(font)
        self.time_reset.setStyleSheet("QPushButton{\n"
"background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #fd8a44; \n"
"    border-color: #fd8a44; \n"
"}")
        self.time_reset.setObjectName("time_reset")
        self.time_start = QtWidgets.QPushButton(self.watchFrame)
        self.time_start.setGeometry(QtCore.QRect(10, 70, 141, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_start.sizePolicy().hasHeightForWidth())
        self.time_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time_start.setFont(font)
        self.time_start.setStyleSheet("QPushButton{\n"
"background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #fd8a44; \n"
"    border-color: #fd8a44; \n"
"}")
        self.time_start.setObjectName("time_start")
        self.time_screen = QtWidgets.QLabel(self.watchFrame)
        self.time_screen.setGeometry(QtCore.QRect(10, 8, 321, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_screen.sizePolicy().hasHeightForWidth())
        self.time_screen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.time_screen.setFont(font)
        self.time_screen.setStyleSheet("background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;")
        self.time_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.time_screen.setObjectName("time_screen")
        self.time_stop = QtWidgets.QPushButton(self.watchFrame)
        self.time_stop.setGeometry(QtCore.QRect(191, 70, 141, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_stop.sizePolicy().hasHeightForWidth())
        self.time_stop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time_stop.setFont(font)
        self.time_stop.setStyleSheet("QPushButton{\n"
"background-color: #171717;\n"
"color: white;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #fd8a44; \n"
"    border-color: #fd8a44; \n"
"}")
        self.time_stop.setObjectName("time_stop")
        self.background_label.raise_()
        self.label.raise_()
        self.title.raise_()
        self.realTimeViewFrame.raise_()
        self.current_mode.raise_()
        self.label_6.raise_()
        self.up_down.raise_()
        self.movment.raise_()
        self.label_11.raise_()
        self.rotGripper.raise_()
        self.gripper.raise_()
        self.title_2.raise_()
        self.turning_bg.raise_()
        self.rempFrame.raise_()
        self.rovStatusFrame.raise_()
        self.label_19.raise_()
        self.fps.raise_()
        self.manual_mode.raise_()
        self.autonmous_mode.raise_()
        self.stabilize_mode.raise_()
        self.depth_hold_mode.raise_()
        self.takephoto.raise_()
        self.label_16.raise_()
        self.camera_frame.raise_()
        self.camera.raise_()
        self.turning.raise_()
        self.watchFrame.raise_()
        VortexGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(VortexGUI)
        QtCore.QMetaObject.connectSlotsByName(VortexGUI)

    def retranslateUi(self, VortexGUI):
        _translate = QtCore.QCoreApplication.translate
        VortexGUI.setWindowTitle(_translate("VortexGUI", "MainWindow"))
        self.current_mode.setText(_translate("VortexGUI", "  Current Mode: "))
        self.title.setText(_translate("VortexGUI", "<html><head/><body><p> &nbsp; Vortex  <font color=\"#fd8a44\">Robotics</font> </p></body></html>\n"
""))
        self.compass_label.setText(_translate("VortexGUI", "  Compass:"))
        self.pressure.setText(_translate("VortexGUI", "  Pressure:"))
        self.depth.setText(_translate("VortexGUI", "  Depth:"))
        self.rov_name_2.setText(_translate("VortexGUI", "Real Time View"))
        self.label_6.setText(_translate("VortexGUI", "Movments"))
        self.label_11.setText(_translate("VortexGUI", "Grippers"))
        self.title_2.setText(_translate("VortexGUI", "<html><head/><body><p align=\"right\">  Team <span style=\" color:#fd8a44;\">Name</span></p>&nbsp;&nbsp;</body></html>"))
        self.offset_button.setText(_translate("VortexGUI", "Offset"))
        self.temperature.setText(_translate("VortexGUI", "  Temp:"))
        self.label_14.setText(_translate("VortexGUI", "Joystick Status"))
        self.label_9.setText(_translate("VortexGUI", "Exploring Depths, Unveiling Secrets: navigate the unknown."))
        self.rov_name.setText(_translate("VortexGUI", "SOBEK 2024"))
        self.label_8.setText(_translate("VortexGUI", "ROV Status"))
        self.label_12.setText(_translate("VortexGUI", "Light Status"))
        self.label_10.setText(_translate("VortexGUI", "Socket Status"))
        self.label_19.setText(_translate("VortexGUI", "<html><head/><body><p><span style=\" color:#fd8a44;\">4k</span></p></body></html>"))
        self.fps.setText(_translate("VortexGUI", "  - 32FPS"))
        self.manual_mode.setText(_translate("VortexGUI", "Manual"))
        self.autonmous_mode.setText(_translate("VortexGUI", "Autonomus"))
        self.stabilize_mode.setText(_translate("VortexGUI", "Stabilize"))
        self.depth_hold_mode.setText(_translate("VortexGUI", "Depth Hold"))
        self.label_16.setText(_translate("VortexGUI", "3D-Model"))
        self.time_reset.setText(_translate("VortexGUI", "Reset"))
        self.time_start.setText(_translate("VortexGUI", "Start"))
        self.time_screen.setText(_translate("VortexGUI", "15:00"))
        self.time_stop.setText(_translate("VortexGUI", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VortexGUI = QtWidgets.QMainWindow()
    ui = Ui_VortexGUI()
    ui.setupUi(VortexGUI)
    VortexGUI.show()
    sys.exit(app.exec_())
