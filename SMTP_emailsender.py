import email.message
import smtplib
import socket

# Récupération des données pour les champs du courriel
mail_from: str = input("Mail from: ")
mail_to: str = input("Mail to: ")
subject: str = input("Subject: ")

print("Body: (enter '.' on a single line to finish typing)")
body = ""
buffer = ""
while (buffer != ".\n"):
    body += buffer
    buffer = input() + '\n'

# Création de l'objet courriel avec EmailMessage

message = email.message.EmailMessage()
message["From"] = mail_from
message["To"] = mail_to
message["Subject"] = subject
message.set_content(body)

#Envoi du courriel avec le protocole SMTP par le serveur de l'université Laval

try:
    with smtplib.SMTP(host="smtp.ulaval.ca", timeout=10) as connection:
        connection.send_message(message)
        print("Message envoyé avec succès.")
except smtplib.SMTPException:
    print("Le mesage n'a pas pu être envoyé")
except socket.timeout:
    print("La connexion au serveur SMTP n'a pas pu être établie.")
