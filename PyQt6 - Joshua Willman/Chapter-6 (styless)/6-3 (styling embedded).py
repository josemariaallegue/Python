import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(230, 140)
        self.setWindowTitle("Style Sheets Example 2")

        label = QLabel("<p align=center>Push a button.</p>")

        normal_button = QPushButton("Normal")

        warning_button = QPushButton("Warning!")
        warning_button.setObjectName("Warning_Button")  # Set ID Selector

        v_box = QVBoxLayout()
        v_box.addWidget(label)
        v_box.addWidget(normal_button)
        v_box.addWidget(warning_button)

        self.setLayout(v_box)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open(r"Chapter-6 (styless)\styles.css", "r") as file:
        styles = file.read()

    app.setStyleSheet(styles)
    window = MainWindow()
    sys.exit(app.exec())
