from PySide6 import QtCore


class VideoStream(QtCore.QObject):
    def __init__(self) -> None:
        super().__init__()
