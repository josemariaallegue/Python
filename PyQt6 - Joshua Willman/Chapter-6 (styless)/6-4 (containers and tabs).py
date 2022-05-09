import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QLineEdit, QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setFixedSize(400, 200)
        self.setWindowTitle("Containers example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        tabBar = QTabWidget()
        self.profileTab = QWidget()
        self.backgroundTab = QWidget()

        self.setUpProfileTab()
        self.setUpBackgroundTab()

        tabBar.addTab(self.profileTab, "Profile details")
        tabBar.addTab(self.backgroundTab, "Background")

        self.setCentralWidget(tabBar)

    def setUpProfileTab(self):
        nameLabel = QLabel("Name")
        nameEdit = QLineEdit()

        addressLabel = QLabel("Address")
        addressEdit = QLineEdit()

        maleRadio = QRadioButton("Male")
        femaleRadio = QRadioButton("Female")

        hLayout = QHBoxLayout()
        hLayout.addWidget(maleRadio)
        hLayout.addWidget(femaleRadio)

        genderBox = QGroupBox("Gender")
        genderBox.setLayout(hLayout)

        vLayout = QVBoxLayout()
        vLayout.addWidget(nameLabel)
        vLayout.addWidget(nameEdit)
        vLayout.addStretch()
        vLayout.addWidget(addressLabel)
        vLayout.addWidget(addressEdit)
        vLayout.addStretch()
        vLayout.addWidget(genderBox)

        self.profileTab.setLayout(vLayout)

    def setUpBackgroundTab(self):

        educationLevels = ["High School Diploma", "Associate's Degree",
                           "Bachelor's Degree", "Master's Degree", "Doctorate or Higher"]

        vLayout = QVBoxLayout()

        for level in educationLevels:
            vLayout.addWidget(QRadioButton(level))

        educationBox = QGroupBox("Highest level of education")
        educationBox.setLayout(vLayout)

        vLayout2 = QVBoxLayout()
        vLayout2.addWidget(educationBox)

        self.backgroundTab.setLayout(vLayout2)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
