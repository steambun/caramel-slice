from crypt import methods
from wsgiref.util import guess_scheme
from flask import Flask, render_template, request, session
from numpy import true_divide
from quaddle_engine import (chooseRandomWord,formatGuessString,formatEmptyGuessString,generateWordList,
                            isValidWord, isValidWordInWordList,generateHint)


app = Flask(__name__)

# The secret key is used to cryptographically-sign the cookies used for storing the session data
app.secret_key = "b'\x0ew\x03\x8a\xe0\x1d_p\xb5\xeb\xecCO\x8f\xe3Z'"

@app.route("/")
def index():

    session['guess_list']=[]
    session['display_error']=""
    session['display_guess_tickcross']="" 
    session['random_word'] = chooseRandomWord(generateWordList())
    session['display_hint'] = generateHint(session['random_word'])
    session['display_last_guess'] = formatEmptyGuessString()

    print("Randomly word chosen: '"+session.get('random_word')+"'")
    print("Generated hint: '"+session['display_hint']+"'")
    return render_template('index.html')

@app.route("/guess_submitted",methods=['GET','POST'])
def game():
    
    session['display_error'] =""
    if request.method== 'POST':
        guess = request.form.get('guess')
        if not isValidWord(guess):
            session['display_error'] = "Your guess is not valid"
        elif not isValidWordInWordList(guess,generateWordList()):
            session['display_error'] = "Your guess is not in the dictionary"
        else:
            # add an guess list item including a (i) tick/cross, (ii) guess and (iii) last_guess_display
            session ['display_guess_tickcross'] = "✔" if (session['random_word']==guess) else "❌"
            session['display_last_guess'] = formatGuessString(session['random_word'],guess)
            session['guess_list'].append([session ['display_guess_tickcross'],guess,session['display_last_guess']])
            printable_guesses = "User words guessed:\n"
            for guessDisplayRow in session['guess_list']:
                printable_guesses=printable_guesses+"\t"+guessDisplayRow[1]+"\n"
            print(printable_guesses)

    return render_template('index.html')

