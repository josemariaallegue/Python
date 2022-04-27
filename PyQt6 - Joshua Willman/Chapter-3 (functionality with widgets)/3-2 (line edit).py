import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setMaximumSize(310, 130)
        self.setWindowTitle("QLineEdit")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.textLabel = QLabel("Please enter your name below.", self)
        self.textLabel.move(20, 15)

        self.nameLabel = QLabel("Name:", self)
        self.nameLabel.move(10, 40)

        self.nameLine = QLineEdit(self)
        self.nameLine.resize(210, 20)
        self.nameLine.move(50, 40)

        self.clearButton = QPushButton("Clear", self)
        self.clearButton.move(105, 80)
        self.clearButton.clicked.connect(self.clearName)

        self.okButton = QPushButton("Ok", self)
        self.okButton.move(185, 80)
        self.okButton.clicked.connect(self.acceptName)

    def clearName(self):
        self.nameLine.clear()

    def acceptName(self):
        print(self.nameLine.text())
        self.close()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
