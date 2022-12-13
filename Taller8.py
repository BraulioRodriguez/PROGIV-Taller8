### Programacion de Computadoras IV
## Taller 8
# Braulio Rodriguez 8-899-1093


from flask import Flask
from flask_mail import Mail, Message
from threading import Thread


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = 'user@gmail.com'
app.config['MAIL_PASSWORD'] = '123456789'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

with app.app_context():
    msg = Message('Hello', sender='from@gmail.com',
                  recipients=['to@gmail.com'],
                  reply_to='somebodyelse@gmail.com')
    msg.body = "..."
    mail.send(msg)

users = ['user@gmail.com']
with app.app_context():
    with mail.connect() as conn:
        for user in users:
            message = '...'
            subject = "hola, "
            msg = Message(recipients=[user], sender='from@gmail.com',
                          body=message, subject=subject)
            conn.send(msg)


def send_email_thread(msg):
    with app.app_context():
        mail.send(msg)


with app.app_context():
    users = ['user@gmail.com']
    for user in users:
        message = '...'
        subject = "hello, "
        msg = Message(recipients=[user], sender='from@gmail.com',
                      body=message, subject=subject)
        thr = Thread(target=send_email_thread, args=[msg])
        thr.start()
