from crypt import methods
from flask import Flask, render_template, request, session
from quaddle_engine import chooseRandomWord,formatGuessString,generateWordList,isValidWord, isValidWordInWordList,generateHint


app = Flask(__name__)

# The secret key is used to cryptographically-sign the cookies used for storing the session data
app.secret_key = "b'\x0ew\x03\x8a\xe0\x1d_p\xb5\xeb\xecCO\x8f\xe3Z'"

@app.route("/")
def index():

    session['guess_list']=[]
    session['display_error']=""
    session['random_word'] = chooseRandomWord(generateWordList())
    session['display_hint'] = generateHint(session['random_word'])
    session['display_last_guess'] = formatGuessString(session['random_word'],session['guess_list'])

    print("Randomly word chosen: '"+session.get('random_word')+"'")
    print("Generated hint: '"+session['display_hint']+"'")
    return render_template('index.html',display_last_guess=session.get('display_last_guess'))

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
            session['guess_list'].append(guess)
            session['display_last_guess'] = formatGuessString(session['random_word'],session['guess_list'])
            printable_guesses = "User words guessed:\n"
            for guess in session['guess_list']:
                printable_guesses=printable_guesses+"\t"+guess+"\n"
            print(printable_guesses)

    return render_template('index.html')