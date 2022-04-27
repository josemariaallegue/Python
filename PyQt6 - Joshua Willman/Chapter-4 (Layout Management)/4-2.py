import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QButtonGroup, QVBoxLayout, QCheckBox


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setMinimumSize(350, 200)
        self.setWindowTitle("QVBoxLayout Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):

        self.chezLabel = QLabel("Chez PyQt6")
        self.chezLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.rateLabel = QLabel("How would you rate your service?")

        ratings = ("Satisfied", "Average", "Not satisfied")
        self.ratingsGroup = QButtonGroup(self)
        self.ratingsGroup.buttonClicked.connect(self.checkboxClicked)

        self.confirmButton = QPushButton("Confirm")
        self.confirmButton.setEnabled(False)
        self.confirmButton.clicked.connect(self.close)

        mainVBox = QVBoxLayout()
        mainVBox.addWidget(self.chezLabel)
        mainVBox.addWidget(self.rateLabel)

        for rating in ratings:
            self.ratingCheck = QCheckBox(rating)
            self.ratingsGroup.addButton(self.ratingCheck)
            mainVBox.addWidget(self.ratingCheck)

        mainVBox.addWidget(self.confirmButton)
        self.setLayout(mainVBox)

    def checkboxClicked(self, button):
        """Check if a QCheckBox in the button group has
        been clicked."""
        print(button.text())
        self.confirmButton.setEnabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
