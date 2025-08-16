import sys

from PySide6.QtWidgets import QApplication

from app.controller.main_controller import MainController
from app.logger import logger, setup_logger
from app.model.video_stream import VideoStream
from app.view.main_window import MainWindow

setup_logger(app_name='PopuLyze', app_author='redzuone', log_file_suffix='populyze')
logger.debug('Starting..')


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
