from PySide6 import QtCore, QtWidgets

from app.view.custom_widgets import JoystickButton


class CameraView(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Camera')
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DontCreateNativeAncestors)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_NativeWindow)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

    def closeEvent(self, event: QtCore.QEvent) -> None:
        self.hide()
        # Ignore to prevent other windows from being un-interactable
        event.ignore()


class CameraControlView(QtWidgets.QWidget):
    play_clicked = QtCore.Signal()
    stop_clicked = QtCore.Signal()

    def __init__(self) -> None:
        super().__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        play_btn = QtWidgets.QPushButton('Play')
        layout.addWidget(play_btn, 0, 0)
        play_btn.clicked.connect(self.play_clicked.emit)
        stop_btn = QtWidgets.QPushButton('Stop')
        layout.addWidget(stop_btn, 1, 0)
        stop_btn.clicked.connect(self.stop_clicked.emit)
        self.joystick_btn = JoystickButton()
        layout.addWidget(self.joystick_btn)
        self.joystick_btn.setFixedSize(45, 45)
