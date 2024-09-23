""" 
Remember the following:
    1. try UDP and know why it is not working
    2. try changing jpeg quality at both ends
    3. try increasing maxSize
    4. consider reducing the frame rate slightly
    5. try using NetGear_Async instead of NetGear
"""


import time
import cv2
import numpy as np
import sys
from queue import Queue
from vidgear.gears import NetGear
import threading

class NetgearClient:
    """
    Create a tcp Netgear Client object
    
    Args:
        address (str): IP address of the server
        port (str): Port number of the server
        options (dict): Options for the Netgear object
    """

    def __init__(self,Address="192.168.33.100",Port="5454") -> None:
        options = {
            "jpeg_compression": True,
            "jpeg_compression_quality": 50,
            "jpeg_compression_fastdct": True,
            "jpeg_compression_fastupsample": True
            # "compression_format": ".png",  # Using PNG format for compression
            # "compression_param": 3,        # Compression level (0 to 9)
        }
        self.client = NetGear(
            receive_mode=True,
            address=Address,
            port=Port,
            protocol="tcp",
            pattern=1,
            logging=True,
            **options
        )

def main():
    """
    Main function to run the client
    """
    # Create the client object
    Client = NetgearClient()
    t = time.time()
    # Loop to receive frames
    for i in range(5000):
        # Receive frames from the server
        time1 = time.time()
        frame = Client.client.recv()
        time2 = time.time()
        print("recv time = ",time2-time1)

        # If NoneType
        if frame is None:
            break
        # Display the frame
        time1 = time.time()
        cv2.imshow("frame",cv2.flip(frame,0))
        time2 = time.time()
        print("imshow time = ",time2-time1)
        cv2.waitKey(1)
    # Calculate the frame rate
    print(5000/(time.time()-t))
    # Close the stream
    Client.client.close()

if __name__ == "__main__":
    main()

