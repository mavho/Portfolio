from flask import Flask
from server.config import Config
import os


app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = app.config['SECRET_KEY']

import server.routes