import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox


class MainWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setGeometry(200, 200, 180, 130)
        self.setMaximumSize(300, 300)
        self.setWindowTitle("Checkbox")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.textLabel = QLabel(
            "Which shifts can you work?\ncheck all that apply", self)
        self.textLabel.move(10, 10)

        self.morningCheck = QCheckBox("Morning [8AM - 2PM]", self)
        self.morningCheck.move(10, 50)
        self.morningCheck.toggled.connect(self.printSelection)

        self.afternoonCheck = QCheckBox("Afetenoon [1PM - 8PM]", self)
        self.afternoonCheck.move(10, 70)
        self.afternoonCheck.toggled.connect(self.printSelection)

        self.nightCheck = QCheckBox("Night [7PM - 3AM]", self)
        self.nightCheck.move(10, 90)
        self.nightCheck.toggled.connect(self.printSelection)

    # checked esta porque toggle envia true o false segun el estado del checkbox
    def printSelection(self, checked):
        # self.sender() permite determinar que widget genero el evento
        if(checked):
            print(f"{self.sender().text()} selected.")
        else:
            print(f"{self.sender().text()} deselected.")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
