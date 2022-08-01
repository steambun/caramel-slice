from flask import Flask, render_template
from quaddle_engine import chooseRandomWord

app = Flask(__name__)

@app.route("/")
def index():
    random_word = chooseRandomWord()
    return render_template('index.html',random_word=random_word)