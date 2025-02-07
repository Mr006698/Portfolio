from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from datetime import date
import os
from forms import ContactForm

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.add_url_rule('/static/uploads/Parker_David_CV_General.pdf', endpoint='CV', build_only=True)
bootstrap = Bootstrap5(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print('Sending Email')

    return render_template('index.html', contact_form=contact_form, year=date.today().strftime('%Y'))


if __name__ == '__main__':
    app.run(debug=True)
    