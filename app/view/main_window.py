from PySide6 import QtWidgets

from app.view.camera_view import CameraControlView, CameraView
from app.view.data_view import DataView
from app.view.map_view import MapView
from app.view.status_view import StatusView


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.resize(800, 640)
        self.setWindowTitle('PopuLyze')

        main_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self._create_menu_bar()
        content_splitter = QtWidgets.QSplitter()
        layout.addWidget(content_splitter)
        left_panel_container = QtWidgets.QWidget()
        left_layout = QtWidgets.QVBoxLayout()
        left_panel_container.setLayout(left_layout)
        content_splitter.addWidget(left_panel_container)
        left_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )
        right_panel_container = QtWidgets.QWidget()
        right_layout = QtWidgets.QVBoxLayout()
        right_panel_container.setLayout(right_layout)
        right_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )
        content_splitter.addWidget(right_panel_container)

        self.data_view = DataView()
        left_layout.addWidget(self.data_view)
        self.map_view = MapView()
        left_layout.addWidget(self.map_view)

        self.camera_view = CameraView()
        right_layout.addWidget(self.camera_view)

        right_bottom_layout = QtWidgets.QHBoxLayout()
        right_layout.addLayout(right_bottom_layout)
        right_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.camera_control_view = CameraControlView()
        right_bottom_layout.addWidget(self.camera_control_view)
        self.status_view = StatusView()
        right_bottom_layout.addWidget(self.status_view)

        self._create_status_bar()

    def _create_menu_bar(self) -> None:
        self.menu_bar = self.menuBar()

        debug_menu = self.menu_bar.addMenu('Debug')
        test = debug_menu.addAction('Test')
        test.setDisabled(True)
        debug_menu.addSeparator()

    def _create_status_bar(self) -> None:
        self.status_bar = self.statusBar()
