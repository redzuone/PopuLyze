from app.model.video_stream import VideoStream
from app.view.main_window import (
    MainWindow,
)


class MainController:
    def __init__(self, view: MainWindow, video_stream: VideoStream) -> None:
        self.view = view
        self.video_stream = video_stream
        self._connect_signals()

    def _connect_signals(self) -> None:
        pass
