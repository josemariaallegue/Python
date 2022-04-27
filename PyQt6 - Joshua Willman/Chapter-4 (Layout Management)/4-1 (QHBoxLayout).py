import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout


class mainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setMinimumWidth(500)
        self.setFixedHeight(60)
        self.setWindowTitle("QHBoxLayout Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        name_label = QLabel("New Username:")

        name_edit = QLineEdit()
        name_edit.setClearButtonEnabled(True)
        name_edit.textEdited.connect(self.checkUserInput)

        self.accept_button = QPushButton("Confirm")
        self.accept_button.setEnabled(False)
        self.accept_button.clicked.connect(self.close)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(name_label)
        main_h_box.addWidget(name_edit)
        main_h_box.addWidget(self.accept_button)
        self.setLayout(main_h_box)

    def checkUserInput(self, text):
        """Check the length and content of name_edit."""
        if len(text) > 0 and all(t.isalpha() or t.isdigit() for t in text):
            self.accept_button.setEnabled(True)
        else:
            self.accept_button.setEnabled(False)


def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
