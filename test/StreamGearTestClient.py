# Import necessary libraries
from vidgear.gears import CamGear
import cv2

# Define the stream URL or path (this could be RTSP, HTTP, or a file path)
stream_url = "http://127.0.0.1:8080"

# Open a connection to the stream
stream = CamGear(source=stream_url).start()

# Loop to continuously capture frames
while True:
    # Read the frame from the stream
    frame = stream.read()

    # Check if frame is received properly
    if frame is None:
        break

    # Display the frame (for visualization, can be skipped)
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up when done
cv2.destroyAllWindows()
stream.stop()
