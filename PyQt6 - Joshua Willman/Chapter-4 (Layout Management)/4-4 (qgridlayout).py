import sys
import json
from PyQt6.QtCore import Qt
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QGridLayout, QTextEdit


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializaUi()

    def initializaUi(self):
        self.setMinimumSize(500, 300)
        self.setWindowTitle("QGridLayout example")
        self.setUpMainWindow()
        self.loadWidgetValuesFromFile()
        self.show()

    def setUpMainWindow(self):
        # left side
        simpleLabel = QLabel("Simpel daily planner")
        simpleLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        todayLabel = QLabel("· Today's Focus")
        todayLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.todayEdit = QTextEdit()

        notesLabel = QLabel("· Notes")
        notesLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.notesEdit = QTextEdit()

        # right side
        dateLabel = QLabel(str(datetime.today().strftime("%d/%m/%Y")))
        dateLabel.setAlignment(Qt.AlignmentFlag.AlignRight)

        toDoLabel = QLabel("· To do")
        toDoLabel.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(simpleLabel, 0, 0)
        self.mainLayout.addWidget(todayLabel, 1, 0)
        self.mainLayout.addWidget(self.todayEdit, 2, 0, 3, 1)
        self.mainLayout.addWidget(notesLabel, 5, 0)
        self.mainLayout.addWidget(self.notesEdit, 6, 0, 3, 1)
        self.mainLayout.addWidget(dateLabel, 0, 2)
        self.mainLayout.addWidget(toDoLabel, 1, 1, 1, 2)

        for i in range(2, 9):
            auxCheck = QCheckBox()
            auxLine = QLineEdit()
            self.mainLayout.addWidget(auxCheck, i, 1)
            self.mainLayout.addWidget(auxLine, i, 2)

        self.setLayout(self.mainLayout)

    def saveWidgetValues(self):
        """Collect and save the widget values."""
        details = {"focus": self.todayEdit.toPlainText(),
                   "notes": self.notesEdit.toPlainText()}
        remaining_todo = []

        for row in range(2, 9):
            item = self.mainLayout.itemAtPosition(row, 1)
            widget = item.widget()

            if widget.isChecked() == False:
                item = self.mainLayout.itemAtPosition(row, 2)
                widget = item.widget()
                text = widget.text()

                if text != "":
                    remaining_todo.append(text)
                    details["todo"] = remaining_todo

        with open("Files\details.txt", "w") as f:
            f.write(json.dumps(details))

    def closeEvent(self, event):
        """Save widget values when closing the window."""
        self.saveWidgetValues()

    def loadWidgetValuesFromFile(self):
        """Retrieve previous values from the last session."""
        # Check if file exists first
        try:
            with open("Files\details.txt", "r") as f:
                details = json.load(f)
                self.todayEdit.setText(details["focus"])
                self.notesEdit.setText(details["notes"])

                for row in range(len(details["todo"])):
                    item = self.mainLayout.itemAtPosition(
                        row + 2, 2)
                    widget = item.widget()
                    widget.setText(details["todo"][row])

        except FileNotFoundError as error:
            f = open("Files\details.txt", "w")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
