from flask import Flask
from flask_mail import Mail
from server.config import Config
import os


app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = app.config['SECRET_KEY']

mail = Mail(app)

import server.routes