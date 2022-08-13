import pytest
from quaddle_engine import *

#
# formatEmptyGuessString()
#
def test_formatEmptyGuessString():
    assert "_ _ _ _" == formatEmptyGuessString()

#
# formatGuessString()
#
def test_formatGuessString_noLettersMatch():
    assert "_ _ _ _" == formatGuessString("bump","test")

def test_formatGuessString_oneLetterMatchesInRightPlace():
    assert "b _ _ _" == formatGuessString("bump","bowl")

def test_formatGuessString_oneLetterMatchesInWrongPlace():
    assert "_ _ * _" == formatGuessString("bump","debt")

def test_formatGuessString_lastCharacterFormattedIsNotASpace():
    assert " " != formatGuessString("bump","debt")[-1]

def test_formatGuessString_showStarIfLetterAppearsCorrectElsewhere():
    assert "p _ _ _" == formatGuessString("poor","pump")

def test_formatGuessString_onlyShowLetterThatWasGuessedCorrectly():
    assert "p _ _ _" == formatGuessString("pump","poor")


#
# isValidGuessInGuessList()
#
def test_isValidGuessInWordList_containsWord():
    wordList=["test"]
    word="test"
    assert True==isValidGuessInWordList(word,wordList)

def test_isisValidGuessInWordList_doesNotContainWord():
    wordList=["bell"]
    word="test"
    assert False==isValidGuessInWordList(word,wordList)

def test_isisValidGuessInWordList_capitalLetter():
    wordList=["bell"]
    word="Bell"
    assert True==isValidGuessInWordList(word,wordList)


#
# isValidWord()
# 
def test_isValidWord_uppercaseStart():
    assert True==isValidWord("Part")

def test_isValidWord_lowercase():
    assert True==isValidWord("part")

def test_isValidWord_wordTooLong():
    assert False==isValidWord("abcde")

def test_isValidWord_wordTooShort():
    assert False==isValidWord("abc")

def test_isValidWord_wordHasNoApostrophies():
    assert False==isValidWord("Ab's")

# 
# letterExistsInBothWordsInCorrectPlace()
#
def test_letterExistsInBothWordsInCorrectPlace_successful():
    assert True==letterExistsInBothWordsInCorrectPlace("p","poor","pump")

def test_letterExistsInBothWordsInCorrectPlace_unsuccessful():
    assert False==letterExistsInBothWordsInCorrectPlace("p","poor","lump")


#
# generateWordList()
#
def test_generateWordList_populated():
    assert len(generateWordList())>0