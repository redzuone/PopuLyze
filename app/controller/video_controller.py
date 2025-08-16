from app.model.video_service import VideoService
from app.view.main_window import (
    MainWindow,
)


class VideoController:
    def __init__(self, view: MainWindow, video_service: VideoService) -> None:
        self.view = view
        self.video_service = video_service
        self._connect_signals()
        self.setup()

    def setup(self) -> None:
        self.window_id = str(int(self.view.camera_view.winId()))
        self.video_service.set_window_id(self.window_id)

    def _connect_signals(self) -> None:
        self.view.camera_control_view.play_clicked.connect(self.video_service.play)
        self.view.camera_control_view.stop_clicked.connect(self.video_service.stop)
