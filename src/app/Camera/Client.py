import cv2
from vidgear.gears import NetGear
from VideoRecorder import VideoRecorder
from ArucoMarkerDetector import ArucoDetector

class NetgearClient:
    """
    Creates a TCP NetGear Client object to receive frames from the server.
    
    Args:
        address (str): IP address of the server (default: "192.168.33.100")
        port (str): Port number of the server (default: "5454")
    """

    def __init__(self, address="192.168.33.100", port="5454") -> None:
        options = {
            "jpeg_compression": True,
            "jpeg_compression_quality": 80,
            "jpeg_compression_fastdct": True,
            "jpeg_compression_fastupsample": True
        }
        self.client = NetGear(
            receive_mode=True,
            address=address,
            port=port,
            protocol="tcp",
            pattern=1,
            logging=True,
            **options
        )


def main():
    """
    Main function to receive, display, and optionally record frames from the server.
    """
    client = NetgearClient()
    video_recorder = None
    aruco_detector = ArucoDetector()

    while True:
        # Receive frames from the server
        frame = client.client.recv()

        # Break the loop if no frame is received
        if frame is None:
            print("No more frames received. Exiting.")
            break

        # Update the frame for ArUco marker detection
        aruco_detector.update_frame(frame)

        # Display the frame
        flipped_frame = cv2.flip(frame, 0)
        cv2.imshow("Frame", flipped_frame)


        # Check for key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Exit the loop on 'q' key press
            break
        elif key == ord('r') and video_recorder is None:  # Start recording on 'r' key press
            print("Recording started...")
            frame_size = (flipped_frame.shape[1], flipped_frame.shape[0])  # Get the frame size
            video_recorder = VideoRecorder(frame_size)  # Initialize video recorder
            video_recorder.start_recording()
        elif key == ord('s') and video_recorder is not None and video_recorder.recording:  # Stop recording on 's' key press
            video_recorder.stop_recording()
            video_recorder = None

        # If recording, write the frame to the video file
        if video_recorder is not None:
            video_recorder.write_frame(flipped_frame)

    # Release resources
    client.client.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

