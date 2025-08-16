from PySide6 import QtWidgets


class DataView(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QtWidgets.QLabel('Data')
        layout.addWidget(label)
