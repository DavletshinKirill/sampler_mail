from flask import flash, render_template
from .form import EmailForm
from . import email
from ..email import send_email


@email.route("/", methods=['GET', 'POST'])
def input_email():
    form = EmailForm()
    if form.validate_on_submit():
        send_email(form.email.data.lower(), "Welcome", 'You have successfully registered')
        flash("Message is sent")
    return render_template("index.html", form=form, title="Email")






