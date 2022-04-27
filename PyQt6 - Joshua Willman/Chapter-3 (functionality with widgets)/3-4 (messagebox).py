import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setGeometry(200, 200, 250, 200)
        self.setMaximumSize(300, 300)
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.authorLabel = QLabel("Author Catalogue", self)
        self.authorLabel.move(50, 10)

        self.searchLabel = QLabel("Search the index for an author", self)
        self.searchLabel.move(10, 30)

        self.nameLabel = QLabel("Name:", self)
        self.nameLabel.move(10, 50)

        self.nameLine = QLineEdit(self)
        self.nameLine.move(55, 50)
        self.nameLine.resize(190, 20)
        self.nameLine.setPlaceholderText("Enter names as: First Last")

        self.searchButton = QPushButton("Search", self)
        self.searchButton.move(60, 85)
        self.searchButton.clicked.connect(self.searchName)

    def searchName(self):
        try:
            with open(r"Files\authors.txt", "r") as file:
                authors = [line.rstrip("\n") for line in file]

            if(self.nameLine.text() in authors):
                QMessageBox.information(self, "Author Found",
                                        "Author found in catalogue!",
                                        QMessageBox.StandardButton.Ok)
            else:
                answer = QMessageBox.question(self, "Author Not Found",
                    """<p>Author not found in catalogue.</p>
                    <p>Do you wish to continue?</p>""",
                    QMessageBox.StandardButton.Yes | \
                    QMessageBox.StandardButton.No, 
                    QMessageBox.StandardButton.Yes)
                
                if answer == QMessageBox.StandardButton.No:
                    print("Closing application.")
                    self.close()
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error",
                f"""<p>File not found.</p> 
                <p>Error: {error}</p>
                Closing application.""", 
                QMessageBox.StandardButton.Ok)
            self.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
