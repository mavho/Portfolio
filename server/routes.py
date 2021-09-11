from flask import render_template, jsonify, abort, request,flash, send_file
from flask_mail import Message,Mail
from server import app, mail
import sys, os

@app.route('/',methods=['GET'])
def index():
    return render_template('_layouts/base.html'), 200