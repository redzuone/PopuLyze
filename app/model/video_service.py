from PySide6 import QtCore

from app.logger import logger
from app.model.video_streamer_mpv import VideoStreamerMPV


class VideoService(QtCore.QObject):
    def __init__(self) -> None:
        super().__init__()
        self.video_stream_1 = VideoStreamerMPV(id='1', source='rtsp://127.0.0.1')

    def play(self) -> None:
        self.video_stream_1.start()
        logger.debug('start playing video')

    def stop(self) -> None:
        self.video_stream_1.stop()
        logger.debug('stop playing video')

    def set_window_id(self, window_id: str) -> None:
        self.video_stream_1.window_id = window_id
