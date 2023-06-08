"""
    Module for implementing the gui
"""

from pathlib import Path
from string import ascii_lowercase as lowercase
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from ttkbootstrap import dialogs
from hangman import Game


def path():
    """
        Methon that returns the path where the assets are stored
    """

    try:
        try:
            from sys import _MEIPASS
            return _MEIPASS
        except ImportError:
            from sys import _MEIPASS2
            return _MEIPASS2
    except ImportError:
        from os.path import abspath
        return abspath(".")


PATH = Path(path()) / "guiAssets"

root = ttk.Window(title="Hangman", themename="darkly", size=(600, 400))

IMAGES = [
    ImageTk.PhotoImage(Image.open(
        PATH / "hang0.png").resize((250, 250), Image.LANCZOS)),
    ImageTk.PhotoImage(Image.open(
        PATH / "hang1.png").resize((250, 250), Image.LANCZOS)),
    ImageTk.PhotoImage(Image.open(
        PATH / "hang2.png").resize((250, 250), Image.LANCZOS)),
    ImageTk.PhotoImage(Image.open(
        PATH / "hang3.png").resize((250, 250), Image.LANCZOS)),
    ImageTk.PhotoImage(Image.open(
        PATH / "hang4.png").resize((250, 250), Image.LANCZOS)),
    ImageTk.PhotoImage(Image.open(
        PATH / "hang5.png").resize((250, 250), Image.LANCZOS)),
    ImageTk.PhotoImage(Image.open(
        PATH / "hang6.png").resize((250, 250), Image.LANCZOS))
]


def correct():
    """
        Method that gets called when the player wins the game
    """

    dialogs.Messagebox.ok(
        "Correct! Click ok to play again!", "You win!", command=reset)


def gameover():
    """
        Method that gets called when the player loses the game
    """

    turns_image.configure(image=IMAGES[int(game)])
    dialogs.Messagebox.ok(
        f"The word was {game.word}. Better luck next time!", "Game Over", command=reset)


def reset():
    """
        Method that reset the game and the GUI
    """

    game.reset()
    for letter, button in zip(lowercase, buttons):
        root.bind(f"<KeyPress-{l}>", lambda _, letter=letter,
                  button=button: guessed(letter, button))
        button.configure(state="enabled")
    update()


def guessed(letter, button):
    """
        Method that gets called when the player guesses a letter
    """

    root.unbind(f"<KeyPress-{letter}>")
    button.configure(state="disabled")
    game.guess(letter)


def update():
    """
        Method that updates the GUI
    """

    turns_image.configure(image=IMAGES[int(game)])
    guess.set(str(game))


game = Game(gameover, correct, update)

guess = ttk.StringVar(value=str(game))
guess_word = ttk.Label(root, font=("Cascadia Mono", 20), textvariable=guess)
guess_word.grid(row=0, column=1, pady=25)

turns_image = ttk.Label(root, image=IMAGES[6])
turns_image.grid(row=0, column=0, rowspan=2)


frame = ttk.Frame(root)
frame.grid(row=1, column=1, pady=50)

buttons = []

for i, l in enumerate(lowercase):
    b = ttk.Button(frame, text=l, width=3)
    b.configure(command=lambda letter=l, button=b: guessed(letter, button))
    buttons.append(b)
    b.grid(row=i // 6, column=i % 6, padx=5, pady=5)
    root.bind(f"<KeyPress-{l}>", lambda _, letter=l,
              button=b: guessed(letter, button))

root.mainloop()
