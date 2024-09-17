import asyncio
import cv2
from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack
from aiortc.contrib.media import MediaPlayer, MediaRelay
from aiohttp import web

# Global peer connection and relay object
pcs = set()
relay = None

# Video stream track class
class VideoTransformTrack(VideoStreamTrack):
    def __init__(self, track):
        super().__init__()
        self.track = track

    async def recv(self):
        frame = await self.track.recv()
        return frame

# WebRTC signaling
async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    pc = RTCPeerConnection()
    pcs.add(pc)

    # Handle track events
    @pc.on("track")
    async def on_track(track):
        global relay
        if relay is None:
            relay = MediaRelay()

        if track.kind == "video":
            local_video = VideoTransformTrack(relay.subscribe(track))
            pc.addTrack(local_video)

    # Set the remote description and create an answer
    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.Response(
        content_type="application/json",
        text=json.dumps(
            {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
        ),
    )

# Cleanup peer connections
async def cleanup():
    while True:
        await asyncio.sleep(10)
        for pc in pcs:
            if pc.iceConnectionState == "closed":
                pcs.remove(pc)

# Web server setup
async def app_factory():
    app = web.Application()
    app.router.add_post("/offer", offer)
    return app

if __name__ == "__main__":
    web.run_app(app_factory())
