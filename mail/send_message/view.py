from flask import flash, render_template
from .form import EmailForm
from . import email
from ..email import send_email, background_task
import redis
from rq import Queue


email.redis = redis.Redis('localhost', 6379)
email.task_queue = Queue(connection=email.redis)


@email.route("/", methods=['GET', 'POST'])
def input_email():
    form = EmailForm()
    if form.validate_on_submit():
        job = email.task_queue.enqueue(background_task)
        flash("Message is sent")
    return render_template("index.html", form=form, title="Email")






