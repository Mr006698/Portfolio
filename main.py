from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap5
from datetime import date
from email.message import EmailMessage
import smtplib
import os
from forms import ContactForm

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.add_url_rule('/static/uploads/Parker_David_CV_General.pdf', endpoint='CV', build_only=True)
bootstrap = Bootstrap5(app)

def send_email(form: ContactForm) -> None:
    msg = EmailMessage()
    msg.set_content(f'Message From: {form.name.data}\nEmail: {form.email.data}\n\n{form.message.data}')
    msg['Subject'] = f'Message From: {form.name.data}'
    msg['From'] = os.environ.get('EMAIL_HOST_USER')
    msg['To'] = os.environ.get('EMAIL_HOST_USER')

    print(msg.as_string())


@app.route('/')
def index():
    contact_form = ContactForm()
    return render_template('index.html', contact_form=contact_form, year=date.today().strftime('%Y'))


@app.route('/submit', methods=['POST'])
def submit() -> str:
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        send_email(contact_form)
        
    else:
        return jsonify({'ok': False, 'errors': contact_form.errors})
    
    return jsonify({'ok': True})


if __name__ == '__main__':
    app.run(debug=True)
    