from PyQt6.QtWidgets import *
from gui import *
import random


class Logic(QMainWindow, Ui_Hangman):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.man_body.setVisible(False)
        self.man_head.setVisible(False)
        self.man_leftarm.setVisible(False)
        self.man_rightarm.setVisible(False)
        self.man_leftleg.setVisible(False)
        self.man_rightleg.setVisible(False)
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_new.clicked.connect(lambda: self.new_word())

        self.max_attempts = 6
        self.word_to_guess = ''
        self.read_data()
        self.new_word()
        self.guessed_letter = self.input_letter.text().strip()
        print(self.guessed_letter)


    def read_data(self):
        filename = 'words.txt'
        try:
            with open(filename, 'r') as file:
                self.word_list = file.read().splitlines()
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

    def check_word(self):
        if self.max_attempts > 0:
            if self.guessed_letter.isalpha():
                for letter in self.word_to_guess:
                    if self.guessed_letter == self.word_to_guess:
                        pass

            else:
                self.max_attempts -= 1
                self.label_result.setText(f"Incorrect! {self.max_attempts} attempts remaining.")

        else:
            self.new_word()
            self.label_result.setText("You failed to guess the word :(")
            return None

    def submit(self):
        pass

    def new_word(self):
        self.input_letter.clear()
        self.label_result.clear()
        self.word_to_guess = random.choice(self.word_list).lower()
