"""
    Module for handling the entire game, excluding GUI/TUI.
"""

from typing import Callable
from word import random_word


class Game(object):
    """
        The main class for the hangman game itself.
    """

    def __init__(self, gameover_func: Callable, correct_func: Callable, update_func: Callable):
        """
            Initialize the game.
            :param func: The function to be called when the game is over.
        """

        self.word = random_word(5, 10)
        self.turns = 6
        self.guesses = []
        self.gameover = gameover_func
        self.correct = correct_func
        self.update = update_func

    def guess(self, letter: str):
        """
            Record a guess.
            :param letter: The letter to be guessed.
        """

        if not letter in self.guesses:
            self.guesses += letter
        self.update()
        self.update()
        if not letter in self.word:
            self.turns -= 1
            if self.turns == 0:
                self.gameover()
        else:
            if "".join(str(self).split(" ")) == self.word:
                self.correct()
        self.update()

    def __int__(self) -> int:
        """
            Returns the number of turns left
        """

        return self.turns

    def __str__(self) -> str:
        """
            Gets a string representation of the letters.
        """

        s = []
        for chr in self.word:
            if chr in self.guesses:
                s += chr
            else:
                s += "_"

        return " ".join(s)
