from  PyQt5.QtWidgets import QApplication
import sys
from .findChild import UI
from joystick.joystick import JoyStick
from communication.companion_link import CompanionLink

joystick_thread = JoyStick()


app = QApplication(sys.argv)
UIWindow = UI()
companion_link = CompanionLink(address="192.168.33.1", port=12345)

companion_link.connect_client_signal(UIWindow.moving.socket_connection)
companion_link.connect_client_signal(UIWindow.status.socket_connection)
companion_link.connect_client_signal(UIWindow.gripper.socket_connection)
# companion_link.connected_signal.connect(print)

# companion_link.connect_sensors_to_gui_signal(print)
companion_link.connect_sensors_to_gui_signal(UIWindow.readings.handle_sensor_logic)
#companion_link.connect_sensors_to_gui_signal(joystick_thread.get_pressure)

joystick_thread.connect_signal(UIWindow.moving.handle_joystick_logic)
joystick_thread.connect_signal(UIWindow.gripper.handle_joystick_logic)
joystick_thread.connect_signal(UIWindow.modes.handle_joystick_logic)
joystick_thread.connect_signal(UIWindow.status.handle_joystick_logic)

joystick_thread.connect_signal(companion_link.send_control_commands)

joystick_thread.connect_signal(print)

companion_link.start()
joystick_thread.start()

app.exec_()
