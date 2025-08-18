from math import hypot

from PySide6 import QtCore, QtGui, QtWidgets


class JoystickButton(QtWidgets.QPushButton):
    state_changed = QtCore.Signal(float, float)

    def __init__(self) -> None:
        super().__init__()
        self.setCheckable(True)

        self.radius = 40
        self.state = [0.0, 0.0]
        self.spot_position = QtCore.QPoint(0, 0)
        self.circle_size = 12

        self.set_state(0.0, 0.0)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.setChecked(True)
        position = event.position() if hasattr(event, 'position') else event.localPos()
        self.press_position = position
        event.accept()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if not self.isChecked():
            return
        position = event.position() if hasattr(event, 'position') else event.localPos()
        possition_diff = position - self.press_position
        self.set_state(possition_diff.x(), -possition_diff.y())
        event.accept()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.setChecked(False)
        self.set_state(0, 0)
        event.accept()

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        event.accept()

    def doubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        event.accept()

    def get_state(self) -> list[float]:
        return self.state

    def set_state(self, x: float, y: float) -> None:
        # circular mapping
        distance = hypot(x, y)
        direction = [0.0, 0.0]
        if distance != 0.0:
            direction = [x / distance, y / distance]
        else:
            direction = [0.0, 0.0]

        clamped_distance = min(distance, self.radius)
        magnitude = (clamped_distance / self.radius) ** 2
        new_state = [direction[0] * magnitude, direction[1] * magnitude]

        half_width, half_height = self.width() / 2, self.height() / 2
        self.spot_position = QtCore.QPoint(int(half_width * (1 + new_state[0])), int(half_height * (1 - new_state[1])))
        self.update()
        if new_state != self.state:
            self.state = new_state
            self.state_changed.emit(self, self.state)

    def paintEvent(self, ev: QtGui.QPaintEvent) -> None:
        super().paintEvent(ev)
        p = QtGui.QPainter(self)
        p.setBrush(QtGui.QBrush(QtGui.QColor(255, 255, 255, 140)))
        p.setPen(QtGui.QPen(QtGui.QColor(100, 100, 100), 2))
        p.drawEllipse(
            self.spot_position.x() - self.circle_size // 2,
            self.spot_position.y() - self.circle_size // 2,
            self.circle_size,
            self.circle_size,
        )
        p.end()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.set_state(*self.state)
        super().resizeEvent(event)
