from random import random
import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class EmptyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Main Window Template")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        info_label = QLabel("Click on the button and select a fruit.")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fruits = [r"Images\1_apple.png", r"Images\2_pineapple.png",
                       r"Images\3_watermelon.png", r"Images\4_banana.png"]

        self.fruitButton = QPushButton()
        self.fruitButton.setIcon(QIcon(random.choice(self.fruits)))
        self.fruitButton.setIconSize(QSize(60, 60))
        self.fruitButton.clicked.connect(self.changeIcon)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(info_label)
        mainLayout.addWidget(self.fruitButton)

        container = QWidget()
        container.setLayout(mainLayout)

        self.setCentralWidget(container)

    def changeIcon(self):
        self.fruitButton.setIcon(QIcon(random.choice(self.fruits)))
        self.fruitButton.setIconSize(QSize(60, 60))


def main():
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
