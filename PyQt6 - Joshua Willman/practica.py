import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QDateEdit, QTextEdit, QPushButton, QFormLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QDate


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setMinimumSize(500, 400)
        self.setWindowTitle("QFormLayout example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # widgets
        fromLabel = QLabel("Appointment form")
        fromLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        firstName = QLineEdit()
        firstName.setPlaceholderText("First")
        lastName = QLineEdit()
        lastName.setPlaceholderText("Last")

        genderBox = QComboBox()
        genderBox.addItems(["Male", "Female"])

        birthEdit = QDateEdit()
        birthEdit.setDate(QDate.currentDate())
        birthEdit.setMaximumDate(QDate.currentDate())
        birthEdit.setDisplayFormat("dd/MM/yyyy")
        birthEdit.setCalendarPopup(True)

        phoneEdit = QLineEdit()
        phoneEdit.setInputMask("(999) 999-9999;_")

        emailEdit = QLineEdit()

        commentsLabel = QLabel("Comments or messages")

        commentsEdit = QTextEdit()

        infoLabel = QLabel()

        submitButton = QPushButton("Submit")

        namesLayout = QHBoxLayout()
        namesLayout.addWidget(firstName)
        namesLayout.addWidget(lastName)

        submitLayout = QHBoxLayout()
        submitLayout.addWidget(infoLabel)
        submitLayout.addWidget(submitButton)

        mainForm = QFormLayout()
        mainForm.addRow(fromLabel)
        mainForm.addRow("Name", namesLayout)
        mainForm.addRow("Gender", genderBox)
        mainForm.addRow("Date", birthEdit)
        mainForm.addRow("Phone", phoneEdit)
        mainForm.addRow("Email", emailEdit)
        mainForm.addRow(commentsLabel)
        mainForm.addRow(commentsEdit)
        mainForm.addRow(submitLayout)

        self.setLayout(mainForm)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
