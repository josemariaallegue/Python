import sys
from unicodedata import name
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QFileDialog, QVBoxLayout, QInputDialog, QFontDialog, QColorDialog, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initializaUi()

    def initializaUi(self):
        self.setWindowTitle("Dialog classes")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        button1 = QPushButton("QFileDialog")
        button1.clicked.connect(self.fileDiaglog)

        button2 = QPushButton("QInputDialog")
        button2.clicked.connect(self.inputDialog)

        button3 = QPushButton("QFontDialog")
        button3.clicked.connect(self.fontDialog)

        button4 = QPushButton("QColorDialog")
        button4.clicked.connect(self.colorDialog)

        button5 = QPushButton("QMessageBox")
        button5.clicked.connect(self.showMesagge)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button1)
        mainLayout.addWidget(button2)
        mainLayout.addWidget(button3)
        mainLayout.addWidget(button4)
        mainLayout.addWidget(button5)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def fileDiaglog(self):
        file, ok = QFileDialog.getOpenFileName(
            self, "Ejemplo QFileDialog", r"Images")

    def inputDialog(self):
        name, ok1 = QInputDialog.getText(self, "Ingrese su nombre", "Nombre:")
        age, ok2 = QInputDialog.getInt(
            self, "Ingrese su edad", "Edad:", min=10, max=100)
        description, ok3 = QInputDialog.getMultiLineText(
            self, "Ingrese su biografia", "Biografia:")
        item, ok4 = QInputDialog.getItem(
            self, "Seleccione su color favorito", "Color:", ["Azul", "Rojo", "Negro"])
        print(name, ok1)
        print(age, ok2)
        print(description, ok3)
        print(item, ok4)

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        print(font, ok)

    def colorDialog(self):
        color = QColorDialog.getColor()
        print(color)

    def showMesagge(self):
        QMessageBox.about(self, "Prueba de messagebox.about", "La prueba")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
