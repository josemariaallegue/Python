import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from PyQt6.QtGui import QPixmap


class RegistrationWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self) -> None:
        self.setGeometry(800, 300, 240, 265)
        self.setWindowTitle("Registration GUI")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self) -> None:
        self.loginLabel = QLabel("Create new account", self)
        self.loginLabel.move(60, 10)

        self.loginLabel = QLabel(self)
        try:
            with open(r"Images\new_user_icon.png"):
                pixmap = QPixmap(r"Images\new_user_icon.png")
                self.loginLabel.setPixmap(pixmap)
        except Exception as e:
            self.loginLabel.setText(str(e))
        self.loginLabel.move(80, 35)

        self.usernameLabel = QLabel("Username:", self)
        self.usernameLabel.move(10, 110)

        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.resize(160, 20)
        self.usernameEdit.move(70, 110)

        self.fullNameLabel = QLabel("Full name:", self)
        self.fullNameLabel.move(10, 135)

        self.fullNameEdit = QLineEdit(self)
        self.fullNameEdit.resize(160, 20)
        self.fullNameEdit.move(70, 135)

        self.passwordLabel = QLabel("Password:", self)
        self.passwordLabel.move(10, 160)

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.resize(160, 20)
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEdit.move(70, 160)

        self.confirmLabel = QLabel("Confirm:", self)
        self.confirmLabel.move(10, 185)

        self.confirmEdit = QLineEdit(self)
        self.confirmEdit.resize(160, 20)
        self.confirmEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmEdit.move(70, 185)

        self.showCheck = QCheckBox("Show password", self)
        self.showCheck.move(70, 210)
        self.showCheck.toggled.connect(self.showPassword)

        self.signUpButton = QPushButton("Sign Up", self)
        self.signUpButton.resize(220, 25)
        self.signUpButton.move(10, 235)
        self.signUpButton.clicked.connect(self.addUser)

    def showPassword(self, checked) -> None:
        if(checked):
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.confirmEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
            self.confirmEdit.setEchoMode(QLineEdit.EchoMode.Password)

    def addUser(self) -> None:
        try:
            if(self.passwordEdit.text() != self.confirmEdit.text()):
                QMessageBox.warning(
                    self, "Error en carga", "Las contraseañas no coinciden", QMessageBox.StandardButton.Close)

            elif(self.usernameEdit.text() == "" or self.passwordEdit.text() == ""):
                QMessageBox.warning(
                    self, "Error en carga", "El usuario o contraseña se encuentran vacios", QMessageBox.StandardButton.Close)
            else:
                with open(r"Files\users.txt", "a+") as file:
                    file.write("\n" + self.usernameEdit.text() +
                               " " + self.passwordEdit.text())
                QMessageBox.information(
                    self, "Creacion de usuario", "Se ha creado correctamente el usuario", QMessageBox.StandardButton.Close)
                self.close()
        except FileNotFoundError:
            QMessageBox.warning(
                self, "Error en carga", "No fue posible cargar el archivo de usuarios", QMessageBox.StandardButton.Close)
            self.close()


def main():
    app = QApplication(sys.argv)
    window = RegistrationWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
