from distutils.log import error
from errno import EEXIST
import random


#wordFile = open("/usr/share/dict/words")
wordFile=open("wordlist_simple.txt")

def isValidWord (word):
    return len(word) ==4 and not word[0].isupper() and word.find("'") ==-1

def isValidWordInWordList(word,wordList):
    for w in wordList:
        if(w==word):
            return True;
    return False;

def guessWord(guessesRemaining,chosenWord,wordList,guessList):
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
    

    if answer == chosenWord:
        guessedCorrectly=True

    return guessedCorrectly

def displayWord(chosenWord,guessList):
    lastGuess=guessList[-1]
    print("here are your guesses so far:")
    for guess in guessList:
        print("\t"+guess)

    wordToPrint=""
    for count,lastGuessLetter in enumerate(lastGuess):
        # right letter, right place
        if(chosenWord[count]==lastGuessLetter):
            wordToPrint=wordToPrint+lastGuessLetter+" "
        #right letter, wrong place
        elif lastGuessLetter in chosenWord:
            wordToPrint=wordToPrint+"* "
        # wrong letter
        else:
            wordToPrint=wordToPrint+"_ "

    print(wordToPrint)


# create a word list
wordList=[]

# create list of valid words
for dirtyWord in wordFile:
    word=dirtyWord.strip()
    if isValidWord(word):
        # print(word)
        wordList.append(word)
    
# choose word at random
chosenWord = random.choice(wordList)

# ask player to guess a word

guesses=6

guessList=[]

for guess in range(guesses):
    guessedCorrectly = guessWord(guesses,chosenWord,wordList,guessList)
    if(guessedCorrectly):
        print ("well done")
        break
    elif guesses==1:
        print("game over, the correct word was: "+chosenWord)
    else:
        guesses=guesses-1
        print("but it's the wrong word, bad luck")
        displayWord(chosenWord,guessList)
   