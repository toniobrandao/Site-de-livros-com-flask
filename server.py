from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def adivinhe_o_numero():
    return render_template('index.html')