# import required libraries
from vidgear.gears import NetGear
import cv2
import os

# flag to indicate whether to save frames or not
save_frames = False

# flag to indicate whether to save video or not
save_video = False

# Define NetGear Client at Server's IP address and assign a unique port address and other parameters
# !!! change following IP address '192.168.x.xxx' with yours !!!
client = NetGear(
    address="192.168.1.104",
    port="5555",
    protocol="tcp",
    pattern=2,
    receive_mode=True,
    logging=True,
    # **options
)

# loop over
while True:
    # receive data from server
    frame = client.recv()

    # check for frame if None
    if frame is None:
        break

    # SPACE TO SAVE FRAMES
    key = cv2.waitKey(1) & 0xFF
    if key == ord(" "):
        save_frames = not save_frames
        if save_frames:
            print("Saving frames...")
        else:
            print("Stopped saving frames.")

    
    if save_frames:
        # Create a directory if it doesn't exist
        os.makedirs("frames", exist_ok=True)
        # Save the frame
        frame_filename = os.path.join("frames", "frame_{}.jpg".format(len(os.listdir("frames"))))
        cv2.imwrite(frame_filename, frame)
        print("Frame saved:", frame_filename)

    # V to start/stop video saving
    if key == ord("v"):
        save_video = not save_video
        if save_video:
            print("Started saving video...")
            # choose CODEC & choose fps
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            video_out = cv2.VideoWriter('path/output.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0])) #make path here
        else:
            print("Stopped saving video.")
            
            video_out.release()

    # If video should be saved
    if save_video:
        # Write the frame to the video file
        video_out.write(frame)

    # Show output window
    cv2.imshow("Client 5555 Output", frame)

    # check for 'q' key if pressed
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()
