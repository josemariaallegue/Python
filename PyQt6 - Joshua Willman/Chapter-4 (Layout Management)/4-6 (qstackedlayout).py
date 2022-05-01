import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QStackedLayout, QFormLayout, QTextEdit, QLineEdit, QSpinBox, QDoubleSpinBox


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(250, 100)
        self.setWindowTitle("QStackedLayout example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        layoutCombo = QComboBox()
        layoutCombo.addItems(["Image", "Description", "Additional info"])
        layoutCombo.activated.connect(self.switchPage)

        # layout 1
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap(r"Images\norwegian.jpg"))
        imageLabel.setScaledContents(True)

        # layout 2
        formLayout1 = QFormLayout()
        formLayout1.addRow("Breed:", QLabel("Norwegian forest cat"))
        formLayout1.addRow("Origin:", QLabel("Norway"))
        formLayout1.addRow(QLabel("Description"))
        formLayout1.addRow(QTextEdit("""Have a long, sturdy body, long legs 
            and a bushy tail. They are friendly, intelligent, 
            and generally good with people."""))

        page2Widget = QWidget()
        page2Widget.setLayout(formLayout1)

        # layout 3
        formLayout2 = QFormLayout()
        formLayout2.addRow(QLabel("Enter yout cat's info."))
        formLayout2.addRow("Name:", QLineEdit())
        formLayout2.addRow("Color:", QLineEdit())

        ageBox = QSpinBox()
        ageBox.setRange(0, 30)
        formLayout2.addRow("Age:", ageBox)

        weightBox = QDoubleSpinBox()
        weightBox.setRange(0.0, 30.0)
        formLayout2.addRow("Weight (kg):", weightBox)

        page3Widget = QWidget()
        page3Widget.setLayout(formLayout2)

        # agrupacion final
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(imageLabel)
        self.stackedLayout.addWidget(page2Widget)
        self.stackedLayout.addWidget(page3Widget)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(layoutCombo)
        mainLayout.addLayout(self.stackedLayout)

        self.setLayout(mainLayout)

    def switchPage(self, index):
        self.stackedLayout.setCurrentIndex(index)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
