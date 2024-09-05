import unittest


class Message:

    def __init__(self, msg="") -> None:
        self.throttle = 1500
        self.yaw = 1500
        self.forward = 1500
        self.lateral = 1500

        self.gripper_1 = 0
        self.gripper_2 = 0
        self.light = "0"
        self.rotating_gripper = "O"

        self.armed = 0
        self.flight_mode = "M"
        self.joystick_connect = 0

        if msg:
            self.throttle = int(msg[:4])
            self.yaw = int(msg[4:8])
            self.forward = int(msg[8:12])
            self.lateral = int(msg[12:16])

            self.gripper_1 = int(msg[16])
            self.gripper_2 = int(msg[17])
            self.light = msg[18]
            self.rotating_gripper = msg[19]

            self.armed = int(msg[20])
            self.flight_mode = msg[21]
            self.joystick_connect = int(msg[22])

    def __str__(self) -> str:
        return (
            str(self.throttle)
            + str(self.yaw)
            + str(self.forward)
            + str(self.lateral)
            + str(self.gripper_1)
            + str(self.gripper_2)
            + str(self.light)
            + str(self.rotating_gripper)
            + str(self.armed)
            + str(self.flight_mode)
            + str(self.joystick_connect)
        )

    def __eq__(self, value) -> bool:
        return (
            self.throttle == value.throttle
            and self.yaw == value.yaw
            and self.forward == value.forward
            and self.lateral == value.lateral
            and self.gripper_1 == value.gripper_1
            and self.gripper_2 == value.gripper_2
            and self.light == value.light
            and self.rotating_gripper == value.rotating_gripper
            and self.armed == value.armed
            and self.flight_mode == value.flight_mode
            and self.joystick_connect == value.joystick_connect
        )


class Test(unittest.TestCase):

    def test_create_msg_1(self):
        encoded_msg = Message()

        encoded_msg.throttle = 1600
        encoded_msg.yaw = 1600
        encoded_msg.forward = 1400
        encoded_msg.lateral = 1300
        encoded_msg.gripper_1 = 1
        encoded_msg.gripper_2 = 0
        encoded_msg.light = "H"
        encoded_msg.rotating_gripper = "L"
        encoded_msg.armed = 1
        encoded_msg.flight_mode = "S"
        encoded_msg.joystick_connect = 1

        decoded_msg = Message(str(encoded_msg))
        self.assertTrue(decoded_msg == encoded_msg)

    def test_create_msg_2(self):
        encoded_msg = Message()

        encoded_msg.throttle = 1100
        encoded_msg.yaw = 1000
        encoded_msg.forward = 1100
        encoded_msg.lateral = 1200
        encoded_msg.gripper_1 = 1
        encoded_msg.gripper_2 = 0
        encoded_msg.light = "0"
        encoded_msg.rotating_gripper = "R"
        encoded_msg.armed = 0
        encoded_msg.flight_mode = "A"
        encoded_msg.joystick_connect = 0

        decoded_msg = Message(str(encoded_msg))
        self.assertEqual(decoded_msg, encoded_msg)


if __name__ == "__main__":
    unittest.main()
