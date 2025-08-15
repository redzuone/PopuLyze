import sys
from PySide6.QtWidgets import QApplication
from app.controller.main_controller import MainController
from app.view.main_window import MainWindow
from app.model.video_stream import VideoStream


class MainApp:
    def __init__(self) -> None:
        self.qt_app = QApplication(sys.argv)
        self.window = MainWindow()
        self.video_stream = VideoStream()
        self.controller = MainController(self.window, self.video_stream)

    def run(self) -> None:
        self.window.show()
        sys.exit(self.qt_app.exec())


if __name__ == '__main__':
    app = MainApp()
    app.run()
