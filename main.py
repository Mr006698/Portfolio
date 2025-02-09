from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap5
from datetime import date
from email.message import EmailMessage
import smtplib
import os
from forms import ContactForm

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_KEY', os.urandom(24))
app.add_url_rule('/static/uploads/Parker_David_CV_General.pdf', endpoint='CV', build_only=True)
bootstrap = Bootstrap5(app)

def send_email(form: ContactForm) -> str:
  # Get the environment vars and check.
  EMAIL_HOST = os.environ.get('EMAIL_HOST')
  EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
  EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
  if not EMAIL_HOST:
    return "Environment Variable 'EMAIL_HOST' not found."
  if not EMAIL_HOST_USER:
    return "Environment Variable 'EMAIL_HOST_USER' not found."
  if not EMAIL_HOST_PASSWORD:
    return "Environment Variable 'EMAIL_HOST_PASSWORD' not found."
  
  try:
        
    with smtplib.SMTP(EMAIL_HOST, 587) as connection:
      msg = EmailMessage()
      msg.set_content(f'Message From: {form.name.data}\nEmail: {form.email.data}\n\n{form.message.data}')
      msg['Subject'] = f'Message From: {form.name.data}'
      msg['From'] = EMAIL_HOST_USER
      msg['To'] = EMAIL_HOST_USER

      connection.starttls()
      connection.login(user=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD)
      connection.send_message(msg)

  except smtplib.SMTPHeloError as ex:
    return "The server refused the helo reply."
  except smtplib.SMTPAuthenticationError as ex:
    return "The server didn't accept the username password combination."
  except smtplib.SMTPNotSupportedError as ex:
    return "The AUTH command is not supported by the server."
  except smtplib.SMTPException as ex:
    return "Unknown exception in smtplib."
  
  return "Successfully sent message."


@app.route('/')
def index():
  contact_form = ContactForm()
  return render_template('index.html', contact_form=contact_form, year=date.today().strftime('%Y'))


@app.route('/submit', methods=['POST'])
def submit() -> str:
  contact_form = ContactForm()
  if not contact_form.validate_on_submit():
    return jsonify({'ok': False, 'errors': contact_form.errors})
    
  success = send_email(contact_form)  
  return jsonify({'ok': True, 'success': success})


if __name__ == '__main__':
  app.run(debug=True)
