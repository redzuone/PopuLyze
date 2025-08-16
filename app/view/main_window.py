from PySide6 import QtWidgets

from app.view.camera_view import CameraControlView, CameraView


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.resize(800, 640)
        self.setWindowTitle('PopuLyze')

        main_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.camera_view = CameraView()
        layout.addWidget(self.camera_view)
        self.camera_control_view = CameraControlView()
        layout.addWidget(self.camera_control_view)
