from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from datetime import date
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('index.html', year=date.today().strftime('%Y'))


if __name__ == '__main__':
    app.run(debug=True)
    