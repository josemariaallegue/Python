import imapclient
import os
import pyzmail
import imaplib

print("Searching and reading mails\n")
USER = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
# para aumentar el limite de bytes que puede recibir python
imaplib._MAXLINE = 10000000

with imapclient.IMAPClient("imap.gmail.com", ssl=True) as imap:

    try:
        # login al email
        imap.login(USER, PASSWORD)
        print("Logged in...")

        # seleccion de carpeta
        imap.select_folder("Inbox", readonly=True)
        # print(imap.list_folders())

        # obtencion de id de mails
        UIDs = imap.search(["ALL"])

        for id in UIDs:

            # obtencion del mail en si
            rawMessage = imap.fetch(id, ["BODY[]", "flags"])

            # parseo del mail
            message = pyzmail.PyzMessage.factory(rawMessage[id][b"BODY[]"])

            # obtencion de las partes del mail
            print(message.get_address("From"))
            print(message.get_address("To"))
            print(message.get_address("CC"))
            print(message.get_address("BCC"), "\n")

            # cuerpo en formato texto
            print(message.text_part.get_payload().decode(
                message.text_part.charset), "\n")

            # cuerpo en formato html
            print(message.html_part.get_payload().decode(
                message.html_part.charset))

            break

    except Exception as e:
        print(f"ERROR: {str(e)}")
