from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField,validators
from wtforms.validators import Required, DataRequired, ValidationError

class ContactForm(FlaskForm):
    name = TextField("Name",  [validators.Required("Name required")])
    email = TextField("Email",  [validators.Required("Email required")])
    subject = TextField("Subject",  [validators.Required("Subject required")])
    message = TextAreaField("Message",  [validators.Required("Message required")])
    submit = SubmitField("Send")