from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
  name = StringField(label='name',
                     validators=[DataRequired(message='Please enter your name.')])
  
  email = EmailField(label='email',
                     validators=[DataRequired(message='Please enter an Email address.'),
                                              Email(message='Please enter a valid email address.'),])
  
  message = TextAreaField(label='message',
                          validators=[DataRequired(message='Please enter your message.')])
  