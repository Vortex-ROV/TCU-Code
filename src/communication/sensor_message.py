from communication.message import Message
import unittest

class SensorMessage(Message):
    def __init__(self, msg=b"") -> None:
        self._msg = {
            "pressure": 0.0,
            "temperature": 0.0,
            "depth": 0.0,
            "heading": 0
        }

        self.recreate_msg(msg)
