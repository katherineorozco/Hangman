from PyQt6.QtWidgets import *
from gui import *

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



    def check_word(self):
        pass



    def submit(self):
        pass
