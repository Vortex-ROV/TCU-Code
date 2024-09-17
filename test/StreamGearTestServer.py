# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import StreamGear
import cv2

# open any valid video stream(from web-camera attached at index `0`)
stream = CamGear(source=0).start()

# enable livestreaming and retrieve framerate from CamGear Stream and
# pass it as `-input_framerate` parameter for controlled framerate
stream_params = {"-input_framerate": stream.framerate, "-livestream": True, "logging": True}

# describe a suitable manifest-file location/name
streamer = StreamGear(output="http://127.0.0.1:8080", **stream_params)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # send frame to streamer
    streamer.stream(frame)



# safely close video stream
stream.stop()

# safely close streamer
streamer.close()