"""
    Module for handling the getting of a random word.
"""

from requests import get
from random import randint

URI = "https://random-word-api.herokuapp.com/word?length="

def random_word(minLen: int = 5, maxLen: int = 15) -> str:
    """
        The main function that gets a random word of a random length ranging from minLen to maxLen.
        :param minLen: Minimum length
        :param maxLen: Maximum length
        :return: A random word
        :rtype: str
    """
    res = get(URI + str(randint(minLen, maxLen)))
    return res.json()[0]
