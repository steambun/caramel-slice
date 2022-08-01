import random



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
