import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer,QPoint
from PyQt5.QtGui import QPainter, QColor,QPolygonF
import random

class SpinWheel(QWidget):
    def __init__(self, parent=None):
        super(SpinWheel, self).__init__(parent)
        self.setMinimumSize(300, 300)

        self.colors = [
            QColor(Qt.red),
            QColor(Qt.green),
            QColor(Qt.blue),
            QColor(Qt.yellow),
            QColor(Qt.cyan),
            QColor(Qt.magenta),
            QColor(Qt.darkCyan)
        ]
        self.current_angle = 0
        self.animation_steps = 100
        self.animation_interval = 20
        self.target_angle = 0
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.animate)
        self.animation_timer.setInterval(self.animation_interval)

        self.spin_button = QPushButton("Spin")
        self.spin_button.clicked.connect(self.start_spin)

        layout = QVBoxLayout()
        layout.addWidget(self.spin_button)
        layout.addStretch()
        self.spin_button.setGeometry(0,0,20,20)
        self.setLayout(layout)

    def start_spin(self):
        self.animation_steps = 100  # Reset animation steps
        num_rotations = random.randint(3, 12)
        self.target_angle = num_rotations * 360 + random.randint(0, 359)  # Increment target angle
        self.animation_timer.start()
      
    def animate(self):
        if self.animation_steps > 0:
            self.current_angle += (self.target_angle - self.current_angle) / self.animation_steps
            self.animation_steps -= 1
            self.update()
        else:
            self.animation_timer.stop()
            self.current_angle %= 360
            self.current_angle = round(self.current_angle, 2)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        size = min(self.width(), self.height())
        wheel_radius = size / 2 - 10

        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.current_angle)

        for i, color in enumerate(self.colors):
            angle = 360 / len(self.colors)
            painter.setBrush(color)
            painter.drawPie(int(-wheel_radius), int(-wheel_radius), int(2 * wheel_radius), int(2 * wheel_radius),
                            int(i * angle * 16), int(angle * 16))
        # Draw pointer
        pointer_length = wheel_radius * 0.5  # Adjust pointer length
        pointer_angle = -self.current_angle
        pointer_p1 = QPoint(0, 0)
        pointer_p2 = QPoint(int(pointer_length * math.cos(math.radians(pointer_angle))),
                            int(pointer_length * math.sin(math.radians(pointer_angle))))
        pointer_p3 = QPoint(int((pointer_length - 3) * math.cos(math.radians(pointer_angle + 10))),
                            int((pointer_length - 5) * math.sin(math.radians(pointer_angle + 10))))

        pointer_polygon = QPolygonF([pointer_p1, pointer_p2, pointer_p3])
        painter.setBrush(Qt.black)
        painter.drawPolygon(pointer_polygon)

if __name__ == "__main__":
    import random

    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()
    spin_wheel = SpinWheel()
    layout.addWidget(spin_wheel)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
