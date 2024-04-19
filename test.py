import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QSize, QUrl

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

class PrimeNumberChecker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Prime Number Checker')
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel('Enter a number:')
        self.layout.addWidget(self.label)

        self.number_input = QLineEdit()
        self.layout.addWidget(self.number_input)

        self.check_button = QPushButton('Check')
        self.check_button.clicked.connect(self.check_number)
        self.layout.addWidget(self.check_button)

        self.help_button = QPushButton('Help')
        self.help_button.clicked.connect(self.show_help)
        self.layout.addWidget(self.help_button)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        # Add video player
        self.video_widget = QVideoWidget()
        self.layout.addWidget(self.video_widget)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

    def check_number(self):
        number = self.number_input.text()
        try:
            number = int(number)
            if is_prime(number):
                self.result_label.setText(f'{number} is a prime number.')
            else:
                self.result_label.setText(f'{number} is not a prime number.')
        except ValueError:
            self.result_label.setText('Please enter a valid number.')

    def show_help(self):
        message_box = QMessageBox()
        message_box.setWindowTitle('Help - Prime Numbers')
        message_box.setText('A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.')
        message_box.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PrimeNumberChecker()
    window.show()
    sys.exit(app.exec_())

  

