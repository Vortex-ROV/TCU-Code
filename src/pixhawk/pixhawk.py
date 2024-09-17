import sys
from pymavlink import mavutil
import time

class Pixhawk:
    def __init__(self) -> None:
        self.master = None

    def set_gripper_light_pwm(self, *msg):
        """
        Sets PWM values for the grippers and light based on the input message.

        :param msg: A string representing the gripper and light control.
                    The string should be 4 characters long.
        """
        dic = {0: 0, "0": 0, "L": "01", "R": "10", 1: 5000, "O": "00", "H": 1800}

        try:
            # Convert and send PWM signals based on msg content
            self.master.set_servo(11, dic[msg[0]])
            self.master.set_servo(7, dic[msg[1]])
            self.master.set_servo(12, dic[msg[1]])
            self.master.set_servo(9, dic[msg[2]])
            self.master.set_servo(13, int(dic[msg[3]][0]) * 5000)
            self.master.set_servo(14, int(dic[msg[3]][1]) * 5000)
            self.master.set_servo(10, 2000)
        except KeyError:
            raise ValueError("Invalid character in message for gripper/light control")

    def set_direction_channel_pwm(
        self, channel3: int, channel4: int, channel5: int, channel6: int
    ):
        """
        Sends RC channel override commands to control throttle, yaw, and other directional controls.

        :param channel3: Throttle control value (int).
        :param channel4: Yaw control value (int).
        :param channel5: Forward/backward control value (int).
        :param channel6: Lateral (left/right) control value (int).
        """
        rc_channel_values = [
            1500,
            1500,
            channel3,
            channel4,
            channel5,
            channel6,
            65535,
            65535,
            65535,
        ]
        self.master.mav.rc_channels_override_send(
            self.master.target_system, self.master.target_component, *rc_channel_values
        )

    def arm(self):
        """
        Arms the Pixhawk to engage the motors.
        """
        self.master.arducopter_arm()

    def disarm(self):
        """
        Disarms the Pixhawk to disengage the motors.
        """
        self.master.arducopter_disarm()

    def set_flight_mode(self, mode_char: str):
        """
        Sets the flight mode of the Pixhawk.

        :param mode_char: Character representing the desired flight mode:
                          'M' for MANUAL, 'S' for STABILIZE, 'A' for ALT_HOLD.
        """
        mode = {"M": "MANUAL", "S": "STABILIZE", "A": "ALT_HOLD"}
        modeName = mode.get(mode_char.upper())

        if modeName not in self.master.mode_mapping():
            print(f"Unknown mode: {modeName}")
            print(f"Try: {list(self.master.mode_mapping().keys())}")
            sys.exit(1)

        mode_id = self.master.mode_mapping()[modeName]
        self.master.mav.set_mode_send(
            self.master.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id,
        )

    def set_max_motor_pwm(self, max: int = 1800):
        """
        Sets the maximum PWM value for the motors.

        :param max: Maximum PWM value in microseconds (int), default is 1800.
        """
        if not isinstance(max, int):
            raise TypeError("Max PWM value must be an integer")

        self.master.mav.param_set_send(
            self.master.target_system,
            self.master.target_component,
            b"MOT_PWM_MAX",
            max,
            mavutil.mavlink.MAV_PARAM_TYPE_REAL32,
        )

    def set_min_motor_pwm(self, min: int = 1200):
        """
        Sets the minimum PWM value for the motors.

        :param min: Minimum PWM value in microseconds (int), default is 1200.
        """
        if not isinstance(min, int):
            raise TypeError("Min PWM value must be an integer")

        self.master.mav.param_set_send(
            self.master.target_system,
            self.master.target_component,
            b"MOT_PWM_MIN",
            min,
            mavutil.mavlink.MAV_PARAM_TYPE_REAL32,
        )

    def set_throttle_gain(self, gain: float):
        """
        Sets the joystick throttle gain parameter.

        :param gain: Throttle gain value (float).
        """
        if not isinstance(gain, float):
            raise TypeError("Throttle gain must be a float")

        self.master.mav.param_set_send(
            self.master.target_system,
            self.master.target_component,
            b"JS_THR_GAIN",
            gain,
            mavutil.mavlink.MAV_PARAM_TYPE_REAL32,
        )

    def flight_mode_running_now(self):
        """
        Retrieves and prints the current flight mode of the Pixhawk.
        """
        heartbeats = self.master.recv_match(type="HEARTBEAT", blocking=True)
        mode = mavutil.mode_string_v10(heartbeats)
        print("Flight mode:", mode)
        time.sleep(0.01)