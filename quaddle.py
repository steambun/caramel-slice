import random
from quaddle_engine import chooseRandomWord,formatGuessString,isValidWord,generateWordList,isValidWordInWordList

def guessWord(guessesRemaining,randomWord,wordList,guessList):
    guessedCorrectly=False
    
    answer = ""
    
    while True:
        print("you have "+str(guessesRemaining)+" guesses remaining")
        answer = input("guess the word?\n")
        if(isValidWordInWordList(answer,wordList)):
            print("'"+answer+"' is a valid word")
            guessList.append(answer)
            break
        else:
            print("'"+answer+"' is not a valid word, try again")
    

    if answer == randomWord:
        guessedCorrectly=True

    return guessedCorrectly


# create a word list
wordList= generateWordList()
    
# choose word at random
randomWord = chooseRandomWord(wordList)

# ask player to guess a word
guesses=6
guessList=[]

for guess in range(guesses):
    guessedCorrectly = guessWord(guesses,randomWord,wordList,guessList)
    if(guessedCorrectly):
        print ("well done")
        break
    elif guesses==1:
        print("game over, the correct word was: "+randomWord)
    else:
        guesses=guesses-1
        print("but it's the wrong word, bad luck")
        print("here are your guesses so far:")
        for guess in guessList:
            print("\t"+guess)
        print(formatGuessString(randomWord,guessList))
   