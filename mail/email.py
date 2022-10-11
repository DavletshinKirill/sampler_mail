from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail
import time


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(recipients, subject, message, seconds):
    app = current_app._get_current_object()
    msg = Message(subject, recipients=[recipients])
    msg.body = message
    thr = Thread(target=send_async_email, args=[app, msg])
    time.sleep(seconds)
    thr.start()
    return thr


def background_task():
    print("Hello")
    time.sleep(15)
    print("world!")
