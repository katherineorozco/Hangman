from PyQt6.QtWidgets import *
from gui import *
import random

class Logic(QMainWindow, Ui_Hangman):
    """Class for handling the logic of the Hangman game."""

    def __init__(self) -> None:
        """Initialize the Hangman game logic."""
        super().__init__()
        self.setupUi(self)
        self.correct_letters: list[str] = []
        self.word_list: list[str] = []
        self.max_attempts: int = 9
        self.word_to_guess: str = ''
        self.guessed_letter: str = self.input_letter.text().strip()
        self.read_data()
        self.word_to_guess = random.choice(self.word_list).lower()

        # Hide body parts at the beginning
        self.man_body.setVisible(False)
        self.man_head.setVisible(False)
        self.man_leftarm.setVisible(False)
        self.man_rightarm.setVisible(False)
        self.man_leftleg.setVisible(False)
        self.man_rightleg.setVisible(False)

        # Connect buttons to functions
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_new.clicked.connect(lambda: self.new_word())

    def read_data(self) -> None:
        """Read the word list from a file."""
        filename: str = 'words.txt'
        try:
            with open(filename, 'r') as file:
                self.word_list = file.read().splitlines()
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

    def check_word(self) -> None:
        """Check if the guessed letter is correct and update the game."""
        if self.max_attempts >= 1:
            if self.guessed_letter.isalpha():
                word_display: str = ''

                if self.guessed_letter.lower() not in self.correct_letters:
                    if self.guessed_letter in self.word_to_guess:
                        self.correct_letters.append(self.guessed_letter.lower())

                for letter in self.word_to_guess:
                    if letter.lower() in self.correct_letters or not letter.isalpha():
                        word_display += letter
                        self.label_result.setText("Good guess!")
                    else:
                        word_display += "_"

                self.label_word.setText(word_display)

                if sorted(set(self.word_to_guess)) == sorted(set(self.correct_letters)):
                    self.label_result.setText("You guessed the word! Click New Word to play again.")
                    self.button_submit.setVisible(False)
                    return

                elif self.guessed_letter.lower() not in set(self.word_to_guess.lower()):
                    self.show_body()
                    self.label_result.setText(f"Incorrect! {self.max_attempts} attempts remaining.")
                    self.max_attempts -= 1

            else:
                self.show_body()
                self.label_result.setText(f"Type in a letter.")

        else:
            self.label_result.setText(f"Wrong! It was {self.word_to_guess}. :( \nClick New Word!")

    def show_body(self) -> None:
        """Show hangman's body parts based on the number of incorrect attempts."""
        if self.max_attempts == 6:
            self.man_head.setVisible(True)
        if self.max_attempts == 5:
            self.man_body.setVisible(True)
        if self.max_attempts == 4:
            self.man_leftarm.setVisible(True)
        if self.max_attempts == 3:
            self.man_rightarm.setVisible(True)
        if self.max_attempts == 2:
            self.man_leftleg.setVisible(True)
        if self.max_attempts == 1:
            self.man_rightleg.setVisible(True)

    def submit(self) -> None:
        """Gets the guessed letter and checks it."""
        self.guessed_letter = self.input_letter.text().strip()
        self.input_letter.clear()
        self.check_word()

    def new_word(self) -> None:
        """Start a new round with a new word."""
        self.max_attempts = 9
        self.input_letter.clear()
        self.label_result.clear()
        self.label_word.clear()
        self.button_submit.setVisible(True)
        self.correct_letters = []
        self.word_to_guess = random.choice(self.word_list).lower()