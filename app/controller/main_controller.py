from app.controller.video_controller import VideoController
from app.model.video_service import VideoService
from app.view.main_window import (
    MainWindow,
)


class MainController:
    def __init__(self, view: MainWindow, video_service: VideoService) -> None:
        self.view = view
        self.video_controller = VideoController(view, video_service)
        self._connect_signals()

    def _connect_signals(self) -> None:
        pass
