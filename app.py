from crypt import methods
from flask import Flask, render_template, request
from quaddle_engine import chooseRandomWord,formatGuessString

app = Flask(__name__)

@app.route("/")
def index():

    global random_word
    global guess_list
    global display_last_guess

    guess_list=[]
    random_word = chooseRandomWord()
    display_last_guess = formatGuessString(random_word,guess_list)

    print("Randomly word chosen: '"+random_word+"'")
    return render_template('index.html',display_last_guess=display_last_guess)

@app.route("/guess_submitted",methods=['GET','POST'])
def game():
    
    if request.method== 'POST':
        guess = request.form.get('guess')
        guess_list.append(guess)
        display_last_guess = formatGuessString(random_word,guess_list)

        printable_guesses = "User words guessed:\n"
        for guess in guess_list:
            printable_guesses=printable_guesses+"\t"+guess+"\n"
        print(printable_guesses)

    return render_template('index.html',random_word=random_word,guess_list=guess_list,display_last_guess=display_last_guess)