from collections import UserDict
from pathlib import Path
import os
import imapclient

print("Deleting mails\n")

USER = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASSWORD")

# conexion al servidor
try:
    with imapclient.IMAPClient("imap.gmail.com", ssl=True) as imap:

        # log in
        imap.login(USER, PASSWORD)
        print("Log in")

        # search con readonly seteado a False
        imap.select_folder("Inbox", readonly=False)
        UIDs = imap.search(["FROM", "alleguejosemaria@gmail.com"])

        if(len(UIDs) != 0):
            print(UIDs)
            # marcado de mensajes con el flag de "Deleted"
            imap.delete_messages(UIDs)
            # eliminacion definitiva de los elementos con flag "Deleted" en folder seleccionado
            imap.expunge()
        else:
            print("No se han encontrado mails para borrar")

except Exception as e:
    print(f"Error {str(e)}")
