from flask import render_template, jsonify, abort, request,flash, send_file
from server.forms import ContactForm
from flask_mail import Message,Mail
from server import app, mail
import sys, os

@app.route('/',methods=['GET','POST'])
def index():
    form = ContactForm(request.form)

    if request.method == 'POST':
        if form.validate() == False:
            flash(form.errors)
            return render_template('_layouts/base.html', form=form), 200
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('_layouts/base.html', success=True,form=ContactForm(formdata=None))

    elif request.method == 'GET':
        return render_template('_layouts/base.html',form=form), 200