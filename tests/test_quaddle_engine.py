import pytest
from quaddle_engine import *

def test_formatEmptyGuessString():
    assert "_ _ _ _" == formatEmptyGuessString()