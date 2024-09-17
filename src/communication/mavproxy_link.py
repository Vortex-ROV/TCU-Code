from pymavlink import mavutil
import sys
import time
from communication.message import Message
from communication.sensor_message import SensorMessage
from pixhawk.pixhawk import Pixhawk
from pixhawk.pixhawk_sensors import PixhawkSensors

# from pixhawk_sensors import SensorsCollector


class MavproxyLink:
    def __init__(self, pixhawk: Pixhawk, pix_sensors: PixhawkSensors, ip_address: str = "192.168.33.100", port: int = 14550, baudrate: int = 115200) -> None:
        self.__pixhawk = pixhawk
        self.__pix_sensors = pix_sensors
        self.__pixhawk.master = mavutil.mavlink_connection("udp:" + ip_address + ":" + str(port), baudrate)
        self.__pixhawk.master.wait_heartbeat()

        print("Connected To Mavproxy")

        self.__sensors_msg = SensorMessage()
        self.__old_sensors_msg = SensorMessage()

        self.__pixhawk.set_max_motor_pwm(1800)
        self.__pixhawk.set_min_motor_pwm(1200)

    def control_pixhawk(self, message):
        """
        Parses the input message and sends the corresponding commands to the Pixhawk.

        :param message: A 25-character string representing control signals for throttle, yaw,
                        forward/backward, lateral movement, grippers, light, arm/disarm, flight mode,
                        and throttle gain.
        """
        if len(message) != len(Message().bytes()):
            raise ValueError(
                f"Message must be exactly {len(Message().bytes())} characters long"
            )

        try:
            message = Message(message)

            # Control movement and gripper/light based on the message
            self.__pixhawk.set_direction_channel_pwm(
                message.get_value("throttle"),
                message.get_value("yaw"),
                message.get_value("forward"),
                message.get_value("lateral"),
            )

            self.__pixhawk.set_gripper_light_pwm(
                message.get_value("gripper_1"),
                message.get_value("gripper_2"),
                message.get_value("light"),
                message.get_value("rotating_gripper"),
            )

            # Arm/Disarm the vehicle
            if message.get_value("armed"):
                self.__pixhawk.arm()
            else:
                self.__pixhawk.disarm()

            # Set flight mode
            self.__pixhawk.set_flight_mode(message.get_value("flight_mode"))

            # Set throttle gain based on joystick connection
            self.__pixhawk.set_throttle_gain(2.0 if message.get_value("joystick_connect") == 1 else 1.0)

        except (ValueError, TypeError) as e:
            print(f"Error in control_pixhawk: {e}")

    def collect_sensors(self) -> SensorMessage:
        """
        Collects sensor data from the Pixhawk and returns it as a SensorMessage.

        :return: Sensor data as a SensorMessage object.
        """

        scaled_pressure2 = self.__pix_sensors.get_scaled_pressure2()
        if scaled_pressure2:
            self.__sensors_msg.set_value("pressure", scaled_pressure2[0])
            self.__sensors_msg.set_value("temperature", scaled_pressure2[1])

        depth = self.__pix_sensors.get_depth()
        if depth:
            self.__sensors_msg.set_value("depth", depth)
        
        heading = self.__pix_sensors.get_heading()
        if heading:
            self.__sensors_msg.set_value("heading", heading)

        return self.__sensors_msg
