from crypt import methods
from flask import Flask, render_template, request
from quaddle_engine import chooseRandomWord

app = Flask(__name__)

@app.route("/")
def index():

    return render_template('index.html')

@app.route("/game",methods=['GET','POST'])
def game():
    random_word = chooseRandomWord()

    if request.method== 'POST':
        guess = request.form.get('guess')
        print('This is your guess "'+guess+"'")

    return render_template('game.html',random_word=random_word)