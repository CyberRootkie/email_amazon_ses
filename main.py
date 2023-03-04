import emails
import configparser

config = configparser.ConfigParser()
config.read('config.cg')


# Prepare the email
message = emails.html(
    html="E-mail avec balise <b>html</b>",
    subject="Objet du message",
    mail_from="jb@watussi.fr",
)

# Pièce jointe
message.attach(filename="blackhat.png", content_disposition="inline", data=open("blackhat.png", "rb"))


# Send the email
r = message.send(
    to="jb@watussi.fr", 
    smtp={
        "host": config['DEFAULT']['HOST'], 
        "port": 587, 
        "timeout": 5,
        "user": config['DEFAULT']['USER'],
        "password": config['DEFAULT']['PASSWORD'],
        "tls": True,
    },
)

print(r)
