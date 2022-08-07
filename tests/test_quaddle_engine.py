import pytest
from quaddle_engine import *

def test_formatEmptyGuessString():
    assert "_ _ _ _" == formatEmptyGuessString()

def test_formatGuessString_noLettersMatch():
    assert "_ _ _ _" == formatGuessString("bump","test")

def test_formatGuessString_oneLetterMatchesInRightPlace():
    assert "b _ _ _" == formatGuessString("bump","bowl")

def test_formatGuessString_oneLetterMatchesInWrongPlace():
    assert "_ _ * _" == formatGuessString("bump","debt")

def test_formatGuessString_lastCharacterFormattedIsNotASpace():
    assert " " != formatGuessString("bump","debt")[-1]