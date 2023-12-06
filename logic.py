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
                word_display = ''
                letter_found = False
                for letter in self.word_to_guess:
                    if self.guessed_letter == letter:
                        word_display += letter
                        letter_found = True
                    else:
                        word_display += "_"

                    self.label_word.setText(word_display)

                    if not letter_found:
                        self.max_attempts -= 1
                        self.show_body()
                        self.label_result.setText(f"Incorrect! {self.max_attempts} attempts remaining.")

            else:
                self.max_attempts -= 1
                self.show_body()
                self.label_result.setText(f"Incorrect! {self.max_attempts} attempts remaining.")

        else:
            self.new_word()
            self.label_result.setText(f"Wrong! It was {self.word_to_guess}. :( \nClick New Word!")
            return None

    def show_body(self):
        if self.max_attempts == 5:
            self.man_head.setVisible(True)
        if self.max_attempts == 4:
            self.man_body.setVisible(True)
        if self.max_attempts == 3:
            self.man_leftarm.setVisible(True)
        if self.max_attempts == 2:
            self.man_rightarm.setVisible(True)
        if self.max_attempts == 1:
            self.man_leftleg.setVisible(True)
        if self.max_attempts == 0:
            self.man_rightleg.setVisible(True)

    def submit(self):
        self.check_word()
        self.input_letter.clear()

    def new_word(self):
        self.max_attempts = 6
        self.input_letter.clear()
        self.label_result.clear()
        self.word_to_guess = random.choice(self.word_list).lower()
