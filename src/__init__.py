from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from .ui.design import Ui_VortexGUI
from .app import Backend
from joystick.joystick import JoyStick
from communication.companion_link import CompanionLink

app = QApplication(sys.argv)
VortexGUI = QMainWindow()
ui = Ui_VortexGUI()
ui.setupUi(VortexGUI)
backend = Backend()
backend.setupUi(ui)
VortexGUI.show()
joystick_thread = JoyStick()
companion_link = CompanionLink(address="192.168.33.1", port=12345)
companion_link.connect_client_signal(backend.moving.socket_connection)
companion_link.connect_client_signal(backend.status.socket_connection)
companion_link.connect_client_signal(backend.grippers.socket_connection)
companion_link.connect_sensors_to_gui_signal(backend.readings.handle_sensor_logic)
joystick_thread.connect_signal(backend.moving.handle_joystick_logic)
joystick_thread.connect_signal(backend.grippers.handle_joystick_logic)
joystick_thread.connect_signal(backend.modes.handle_joystick_logic)
joystick_thread.connect_signal(backend.status.handle_joystick_logic)
joystick_thread.connect_signal(companion_link.send_control_commands)
joystick_thread.connect_signal(print)
companion_link.start()
joystick_thread.start()
app.exec_()