import random
import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')
LENGTH_OF_WORD = 4

def generateHint(guess):
    hint = ""
    if(os.environ.get('OPENAI_API_KEY')):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Generate a clue for the word "+guess,
            temperature=0,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        hint=response.choices[0].text
        hint=hint.lower()
        hint=hint.replace("\n","")
        hint=hint.replace(guess,"_ _ _ _")        
        hint=hint.capitalize()

    return hint

def formatEmptyGuessString():   
    wordToDisplay=""
    wordToDisplay+=(LENGTH_OF_WORD-1)*"_ "
    wordToDisplay+="_"

    return wordToDisplay

def formatGuessString(wordToGuess,lastGuess):

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
    return len(word) ==LENGTH_OF_WORD and not word[0].isupper() and word.find("'") ==-1

def isValidWordInWordList(word,wordList):
    for w in wordList:
        if(w==word):
            return True;
    return False;

def generateWordList():
    #wordFile = open("/usr/share/dict/words")
    wordFile=open("wordlist_simple.txt")

    # create a word list
    wordList=[]

    # create list of valid words
    for dirtyWord in wordFile:
        word=dirtyWord.strip()
        if isValidWord(word):
            # print(word)
            wordList.append(word)
    return wordList


def chooseRandomWord(wordList):
    # choose word at random
    return random.choice(wordList)
