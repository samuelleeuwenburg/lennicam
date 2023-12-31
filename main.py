from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from picamera2 import Picamera2
import time
import http.server
import socketserver

picam2 = Picamera2()
video_config = picam2.create_video_configuration({"size": (640, 480)})
picam2.configure(video_config)

encoder = H264Encoder(bitrate=1000000, repeat=True, iperiod=15)
output = FfmpegOutput("-f hls -hls_time 1 -hls_list_size 1 -hls_flags delete_segments -hls_allow_cache 0 public/stream.m3u8", audio=True)

picam2.start_recording(encoder, output)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="./public", **kwargs)

with socketserver.TCPServer(("", 8080), Handler) as httpd:
    httpd.serve_forever()
