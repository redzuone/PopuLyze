from PySide6 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('PopuLyze')

        main_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.hello_label = QtWidgets.QLabel('Hello')
        layout.addWidget(self.hello_label)
