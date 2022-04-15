import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
# QPixmap es para mostrar imagenes
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self) -> None:
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle("Chapter-2")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # creacion de un label
        hello_label = QLabel(self)
        hello_label.setText("Hello")
        hello_label.move(105, 15)

        # incorporacion de una imagen
        image = r"Images\world.png"
        try:
            with open(image):
                # primero creo el label donde ira la imagen
                world_label = QLabel(self)
                # creo un objeto QPixmap con la imagen y la seteo dentro del label
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
