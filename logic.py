from PyQt6.QtWidgets import *
from gui import *
import random


class Logic(QMainWindow, Ui_Hangman):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.correct_letters = []
        self.word_list = []
        self.max_attempts = 9
        self.word_to_guess = ''
        self.guessed_letter = self.input_letter.text().strip()
        self.read_data()
        self.word_to_guess = random.choice(self.word_list).lower()


        self.man_body.setVisible(False)
        self.man_head.setVisible(False)
        self.man_leftarm.setVisible(False)
        self.man_rightarm.setVisible(False)
        self.man_leftleg.setVisible(False)
        self.man_rightleg.setVisible(False)
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_new.clicked.connect(lambda: self.new_word())



    def read_data(self):
        filename = 'words.txt'
        try:
            with open(filename, 'r') as file:
                self.word_list = file.read().splitlines()
        except FileNotFoundError:
            print(f"Error: {filename} not found.")


    def check_word(self):
        print(f"Word to guess: {self.word_to_guess}")
        print(f"Guessed letter: {self.guessed_letter}")

        if self.max_attempts >= 1:
            if self.guessed_letter.isalpha():
                word_display = ''

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

    def show_body(self):
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

    def submit(self):
        self.guessed_letter = self.input_letter.text().strip()
        self.input_letter.clear()
        self.check_word()


    def new_word(self):
        self.max_attempts = 9
        self.input_letter.clear()
        self.label_result.clear()
        self.label_word.clear()
        self.button_submit.setVisible(True)
        self.correct_letters = []
        self.word_to_guess = random.choice(self.word_list).lower()

