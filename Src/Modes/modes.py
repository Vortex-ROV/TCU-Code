from PyQt5.QtWidgets import QWidget


class Modes:
    def __init__(self, current_mode, autonmous_mode, depth_hold_mode,
                            stabilize_mode, manual_mode):
        # super(Modes, self).__init__()


        self.current_mode = current_mode

        self.autonmous_mode = autonmous_mode

        self.depth_hold_mode = depth_hold_mode

        self.stabilize_mode = stabilize_mode

        self.manual_mode = manual_mode

    def handle_joystick_logic(self, data):
        data = data.decode('utf-8')
        mode = data[22]

        if mode=='M':
            self.current_mode.setText("  Current Mode: Manual")
            self.manual_mode.setStyleSheet("background-color: #fd8a44;color: white;border-radius: 5px;")
            self.autonmous_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.depth_hold_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.stabilize_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
        elif mode=='Y':
            self.current_mode.setText("  Current Mode: Autonmous")
            self.autonmous_mode.setStyleSheet("background-color: #fd8a44;color: white;border-radius: 5px;")
            self.manual_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.depth_hold_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.stabilize_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
        elif mode=='A':
            self.current_mode.setText("  Current Mode: Depth Hold")
            self.depth_hold_mode.setStyleSheet("background-color: #fd8a44;color: white;border-radius: 5px;")
            self.autonmous_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.manual_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.stabilize_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
        elif mode=='S':
            self.current_mode.setText("  Current Mode: Stabilize")
            self.stabilize_mode.setStyleSheet("background-color: #fd8a44;color: white;border-radius: 5px;")
            self.autonmous_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.depth_hold_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")
            self.manual_mode.setStyleSheet("background-color: #171717;color: white;border-radius: 5px;")

    def current_modedef(self, clicked_button):
        clicked_button = self.sender()
        button_text = clicked_button.text()
        self.current_mode.setText(f"  Current Mode: {button_text}")

