import random


def formatGuessString(wordToGuess,guessList):

    # if the guess is empty OR guess list is empty
    if(not guessList):
        return "_ _ _ _"

    lastGuess=guessList[-1]

    wordToDisplay=""
    for count,lastGuessLetter in enumerate(lastGuess):
        # right letter, right place
        if(wordToGuess[count]==lastGuessLetter):
            wordToDisplay=wordToDisplay+lastGuessLetter+" "
        #right letter, wrong place
        elif lastGuessLetter in wordToGuess:
            wordToDisplay=wordToDisplay+"* "
        # wrong letter
        else:
            wordToDisplay=wordToDisplay+"_ "

    return wordToDisplay

def isValidWord (word):
    return len(word) ==4 and not word[0].isupper() and word.find("'") ==-1

def chooseRandomWord():
    wordFile=open("wordlist_simple.txt")

    # create a word list
    wordList=[]

    # create list of valid words
    for dirtyWord in wordFile:
        word=dirtyWord.strip()
        if isValidWord(word):
            # print(word)
            wordList.append(word)

    # choose word at random
    return random.choice(wordList)
