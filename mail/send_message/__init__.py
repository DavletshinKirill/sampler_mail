from flask import Blueprint

email = Blueprint('send_message', __name__,  template_folder="../templates")

from . import view
