import smtplib
import os
import imghdr
from email.message import EmailMessage
from pathlib import Path

print("Sending emails\n")

# obtencion de constantes
SENDER = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASSWORD")

# armado del mensaje
message = EmailMessage()
message["Subject"] = "Prueba"
message["From"] = SENDER
message["To"] = "JoseMaria.Allegue@crowe.com.ar"
message.set_content("body")

# para mandar un archivo adjunto hay que leerlo en bits (por lo menos la imagen) y determinar
# el tipo y el nombre
path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-18")

for file in os.listdir(path):
    with open(Path(path, file), "rb") as f:

        file_data = f.read()
        file_name = Path(path, file).name

        # la primera parte es para imagen
        if(f.name.endswith(".jpg")):
            file_type = imghdr.what(f.name)
            message.add_attachment(file_data, maintype="image",
                                   subtype=str(file_type), filename=file_name)
        # la segunda para el resto
        else:
            message.add_attachment(file_data, maintype="application",
                                   subtype="octet_stream", filename=file_name)

            # conexion y envio del mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

    try:
        smtp.login(SENDER, PASSWORD)
        print("Logged in...")
        smtp.send_message(message)
        print("Sent")

    except Exception as e:
        print(f"Error: {str(e)}")
