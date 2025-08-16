from PySide6 import QtWidgets


class StatusView(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QtWidgets.QLabel('Status')
        layout.addWidget(label)
