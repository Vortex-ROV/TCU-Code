from PyQt5.QtWidgets import QWidget
from communication.message import Message


class Modes:
    def __init__(self, ui):
        self.ui = ui

    def handle_joystick_logic(self, data):
        data = Message(data)
        mode = data.get_value("flight_mode")

        if mode=='M':
            self.ui.current_mode.setText("  Current Mode: Manual")
            self.ui.manual_mode.setStyleSheet("background-color: #fd8a44;color: white;border-radius: 5px;")
            self.ui.autonmous_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.ui.depth_hold_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.ui.stabilize_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
        elif mode=='Y':
            self.ui.current_mode.setText("  Current Mode: Autonmous")
            self.ui.autonmous_mode.setStyleSheet("background-color: #fd8a44;color: white;border-radius: 5px;")
            self.ui.manual_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.ui.depth_hold_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.ui.stabilize_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
        elif mode=='A':
            self.ui.current_mode.setText("  Current Mode: Depth Hold")
            self.ui.depth_hold_mode.setStyleSheet("background-color: #fd8a44;color: white;border-radius: 5px;")
            self.ui.autonmous_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.ui.manual_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.ui.stabilize_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
        elif mode=='S':
            self.ui.current_mode.setText("  Current Mode: Stabilize")
            self.ui.stabilize_mode.setStyleSheet("background-color: #fd8a44;color: white;border-radius: 5px;")
            self.ui.autonmous_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.ui.depth_hold_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.ui.manual_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")

    def current_modedef(self, clicked_button):
        clicked_button = self.sender()
        button_text = clicked_button.text()
        self.ui.current_mode.setText(f"  Current Mode: {button_text}")
