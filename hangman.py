"""
    Module for handling the entire game, excluding GUI/TUI.
"""

from typing import Callable
from word import random_word

class Game(object):
    """
        The main class for the hangman game itself.
    """

    def __init__(self, func: Callable):
        """
            Initialize the game.
            :param func: The function to be called when the game is over.
        """

        self.word = random_word()
        self.turns = 6
        self.guesses = []
        self.gameover = func

    def guess(self, letter: str):
        """
            Record a guess.
            :param letter: The letter to be guessed.
        """

        if letter in self.word:
            guesses += letter
        else:
            self.turns -= 1
            if self.turns == 0:
                self.gameover()

    def __int__(self) -> int:
        """
            Returns the number of turns left
        """

        return self.turns
    
    def __str__(self) -> str:
        """
            Gets a string representation of the letters.
        """

        s = ""
        for chr in self.word:
            if chr in self.guesses:
                s += chr
            else:
                s += "_"

        return s
