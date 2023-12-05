# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Hangman(object):
    def setupUi(self, Hangman):
        Hangman.setObjectName("Hangman")
        Hangman.setEnabled(True)
        Hangman.resize(480, 500)
        Hangman.setMinimumSize(QtCore.QSize(480, 500))
        Hangman.setMaximumSize(QtCore.QSize(480, 500))
        self.centralwidget = QtWidgets.QWidget(parent=Hangman)
        self.centralwidget.setObjectName("centralwidget")
        self.line_hangman = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_hangman.setGeometry(QtCore.QRect(370, 50, 41, 231))
        self.line_hangman.setMidLineWidth(8)
        self.line_hangman.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_hangman.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_hangman.setObjectName("line_hangman")
        self.line_hangman_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_hangman_2.setGeometry(QtCore.QRect(280, 30, 111, 51))
        self.line_hangman_2.setLineWidth(1)
        self.line_hangman_2.setMidLineWidth(8)
        self.line_hangman_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_hangman_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_hangman_2.setObjectName("line_hangman_2")
        self.line_hangman_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_hangman_4.setGeometry(QtCore.QRect(270, 50, 21, 41))
        self.line_hangman_4.setMidLineWidth(8)
        self.line_hangman_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_hangman_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_hangman_4.setObjectName("line_hangman_4")
        self.line_hangman_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_hangman_3.setGeometry(QtCore.QRect(350, 270, 71, 31))
        self.line_hangman_3.setMidLineWidth(8)
        self.line_hangman_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_hangman_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_hangman_3.setObjectName("line_hangman_3")
        self.label_guess = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_guess.setGeometry(QtCore.QRect(150, 300, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_guess.setFont(font)
        self.label_guess.setObjectName("label_guess")
        self.button_submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(250, 330, 91, 51))
        self.button_submit.setObjectName("button_submit")
        self.input_letter = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_letter.setGeometry(QtCore.QRect(150, 330, 71, 61))
        self.input_letter.setMaximumSize(QtCore.QSize(16777213, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.input_letter.setFont(font)
        self.input_letter.setText("")
        self.input_letter.setMaxLength(1)
        self.input_letter.setObjectName("input_letter")
        self.label_result = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(130, 400, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setWordWrap(True)
        self.label_result.setObjectName("label_result")
        self.label_word = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_word.setGeometry(QtCore.QRect(60, 200, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_word.setFont(font)
        self.label_word.setObjectName("label_word")
        self.label_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(30, -10, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label_title.setFont(font)
        self.label_title.setWordWrap(True)
        self.label_title.setObjectName("label_title")
        self.man_head = QtWidgets.QLabel(parent=self.centralwidget)
        self.man_head.setGeometry(QtCore.QRect(260, 60, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.man_head.setFont(font)
        self.man_head.setObjectName("man_head")
        self.man_body = QtWidgets.QLabel(parent=self.centralwidget)
        self.man_body.setGeometry(QtCore.QRect(270, 110, 21, 81))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.man_body.setFont(font)
        self.man_body.setObjectName("man_body")
        self.man_rightleg = QtWidgets.QLabel(parent=self.centralwidget)
        self.man_rightleg.setGeometry(QtCore.QRect(280, 180, 21, 61))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.man_rightleg.setFont(font)
        self.man_rightleg.setObjectName("man_rightleg")
        self.man_leftleg = QtWidgets.QLabel(parent=self.centralwidget)
        self.man_leftleg.setGeometry(QtCore.QRect(260, 180, 21, 61))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.man_leftleg.setFont(font)
        self.man_leftleg.setObjectName("man_leftleg")
        self.man_leftarm = QtWidgets.QLabel(parent=self.centralwidget)
        self.man_leftarm.setGeometry(QtCore.QRect(250, 120, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.man_leftarm.setFont(font)
        self.man_leftarm.setObjectName("man_leftarm")
        self.man_rightarm = QtWidgets.QLabel(parent=self.centralwidget)
        self.man_rightarm.setGeometry(QtCore.QRect(270, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.man_rightarm.setFont(font)
        self.man_rightarm.setObjectName("man_rightarm")
        self.button_new = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_new.setGeometry(QtCore.QRect(280, 10, 113, 32))
        self.button_new.setObjectName("button_new")
        Hangman.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Hangman)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 24))
        self.menubar.setObjectName("menubar")
        Hangman.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Hangman)
        self.statusbar.setObjectName("statusbar")
        Hangman.setStatusBar(self.statusbar)

        self.retranslateUi(Hangman)
        QtCore.QMetaObject.connectSlotsByName(Hangman)

    def retranslateUi(self, Hangman):
        _translate = QtCore.QCoreApplication.translate
        Hangman.setWindowTitle(_translate("Hangman", "MainWindow"))
        self.label_guess.setText(_translate("Hangman", "Guess:"))
        self.button_submit.setText(_translate("Hangman", "SUBMIT"))
        self.label_word.setText(_translate("Hangman", "-------"))
        self.label_title.setText(_translate("Hangman", "Guess the word!"))
        self.man_head.setText(_translate("Hangman", "o"))
        self.man_body.setText(_translate("Hangman", "|"))
        self.man_rightleg.setText(_translate("Hangman", "\\"))
        self.man_leftleg.setText(_translate("Hangman", "/"))
        self.man_leftarm.setText(_translate("Hangman", "-"))
        self.man_rightarm.setText(_translate("Hangman", "-"))
        self.button_new.setText(_translate("Hangman", "New Word"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hangman = QtWidgets.QMainWindow()
    ui = Ui_Hangman()
    ui.setupUi(Hangman)
    Hangman.show()
    sys.exit(app.exec())
