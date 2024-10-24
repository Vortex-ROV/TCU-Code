import cv2
from vidgear.gears import NetGear

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
            "jpeg_compression_quality": 50,
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

def setup_video_writer(frame_size, output_filename='D:\Vortex25\FramesUW\output1.mp4'):
    """
    Set up the video writer object.

    Args:
        frame_size (tuple): Size of the frames to record (width, height).
        output_filename (str): Name of the output video file.

    Returns:
        cv2.VideoWriter: The video writer object.
    """
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    return cv2.VideoWriter(output_filename, fourcc, 20.0, frame_size)

def main():
    """
    Main function to receive, display, and optionally record frames from the server.
    """
    client = NetgearClient()
    recording = False
    out = None

    while True:
        # Receive frames from the server
        frame = client.client.recv()

        # Break the loop if no frame is received
        if frame is None:
            print("No more frames received. Exiting.")
            break

        # Display the frame
        flipped_frame = cv2.flip(frame, 0)
        cv2.imshow("Frame", flipped_frame)

        # If recording, write the frame to the video file
        if recording and out is not None:
            out.write(flipped_frame)

        # Check for key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Exit the loop on 'q' key press
            break
        elif key == ord('r') and not recording:  # Start recording on 'r' key press
            print("Recording started...")
            frame_size = (flipped_frame.shape[1], flipped_frame.shape[0])  # Get the frame size
            out = setup_video_writer(frame_size)  # Initialize video writer
            recording = True
        elif key == ord('s') and recording:  # Stop recording on 's' key press
            print("Recording stopped.")
            recording = False
            if out is not None:
                out.release()  # Release video writer

    # Release resources
    client.client.close()
    if out is not None:
        out.release()  # Make sure video writer is released if still recording
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

