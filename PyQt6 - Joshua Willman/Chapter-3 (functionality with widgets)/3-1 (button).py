import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("pushButton example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.timesPressed = 0

        self.textLabel = QLabel("Don't push the pushButton", self)
        self.textLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textLabel.move(60, 30)

        self.pushButton = QPushButton("Push me", self)
        self.pushButton.move(80, 70)
        # manejo de un evento, en este caso un click
        # se conecta el envento a una funcion
        self.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.timesPressed += 1

        if(self.timesPressed == 1):
            self.textLabel.setText("Why'd you press me?")
        elif(self.timesPressed == 2):
            self.textLabel.setText("I'm warning you.")
            self.pushButton.setText("Feelin' Lucky?")
            self.pushButton.adjustSize()
            self.pushButton.move(70, 70)
        elif(self.timesPressed == 3):
            print("The window has been closed.")
            self.close()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
