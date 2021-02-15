from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox, QLabel
import sys


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.turn_player = 1
        self.reset = QtWidgets.QPushButton(self)
        self.setGeometry(200, 200, 800, 550)
        self.setWindowTitle("welcome to this Game of TicTacToe")
        # Do I need to create this before I can append stuff to it?

        self.name_one = QInputDialog.getText(self, 'Welcome', 'Player 1, please enter your name:')
        print(self.name_one)
        print(type(self.name_one))
        self.name_two = QInputDialog.getText(self, 'Welcome', 'Player 2, please enter your name:')
        self.players = {0: self.name_one[0], 1: self.name_two[0]}
        self.message = QMessageBox()

        self.player1_score = QLabel(self)
        self.player1_name = QLabel(self)
        self.player1 = 0
        self.player2_score = QLabel(self)
        self.player2_name = QLabel(self)
        self.player2 = 0
        self.initUI()

        y_coordinate = 50
        self.buttons = [[0] * 3 for i in range(3)]
        for row in range(3):
            x_coordinate = 50
            for column in range(3):
                # This is a list and the index doesn't exist yet, so you have to "append" the button to the list.
                # Only after there is an object at that index is when you can manipulate objects using indexes.
                self.buttons[row][column] = QtWidgets.QPushButton(self)
                self.buttons[row][column].setText(" ")
                # The first two integers represent the coordinates of the button and the other two are for the size.
                self.buttons[row][column].setGeometry(x_coordinate, y_coordinate, 120, 120)
                # QUESTION: Why is it that when I put the brackets after button_clicked, it doesn't work (the method
                # runs multiple times)
                self.buttons[row][column].clicked.connect(self.button_clicked)
                x_coordinate += 150
            y_coordinate += 150

    def initUI(self):
        self.reset.setText("Reset")
        self.reset.setGeometry(500, 300, 120, 50)
        self.reset.setStyleSheet("border: 1px solid black;")
        self.reset.clicked.connect(self.button_clicked)

        self.player1_score.setText(str(self.player1))
        self.player1_score.setGeometry(500, 120, 120, 50)
        self.player1_score.setStyleSheet("border: 1px solid black;")
        self.player1_score.setAlignment(Qt.AlignCenter)

        self.player1_name.setText(self.name_one[0])
        self.player1_name.setGeometry(500, 50, 120, 50)
        self.player1_name.setStyleSheet("border: 1px solid black;")
        self.player1_name.setAlignment(Qt.AlignCenter)

        self.player2_score.setText(str(self.player2))
        self.player2_score.setGeometry(650, 120, 120, 50)
        self.player2_score.setStyleSheet("border: 1px solid black;")
        self.player2_score.setAlignment(Qt.AlignCenter)

        self.player2_name.setText(self.name_two[0])
        self.player2_name.setGeometry(650, 50, 120, 50)
        self.player2_name.setStyleSheet("border: 1px solid black;")
        self.player2_name.setAlignment(Qt.AlignCenter)

    def button_clicked(self):
        sender = self.sender()
        if sender == self.reset:
            for i in range(len(self.buttons)):
                for y in range(len(self.buttons[i])):
                    self.buttons[i][y].setText(" ")
            self.player1_score.setText("")
            self.player2_score.setText("")
            self.player1 = 0
            self.player2 = 0
            self.update()
        elif self.turn_player % 2 == 1:
            sender.setText("X")
            self.turn_player += 1
            self.update()
            self.check_won()
        else:
            sender.setText("O")
            self.turn_player += 1
            self.update()
            self.check_won()

    def check_won(self):
        check_empty = False
        for row in range(3):
            for button in range(3):
                if self.buttons[row][button].text() != "X" and self.buttons[row][button].text() != "O":
                    check_empty = True
        if not check_empty:
            print("DRAW")
            self.message.setText("It is a draw!")
            self.update()
            self.message.show()
        elif self.check_winner():
            print("Congratulations player {}, you won!".format(self.players[self.turn_player % 2]))
            self.message.setText("Congratulations player {}, you won!".format(self.players[self.turn_player % 2]))
            if self.turn_player % 2:
                self.player2 += 1
            else:
                self.player1 += 1
            self.update()
            self.message.show()

    def update(self):
        self.player1_score.setText(str(self.player1))
        self.player2_score.setText(str(self.player2))
        self.repaint()

    def check_winner(self):
        if (self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text()) and (
                self.buttons[0][0].text() != " "):
            print("THIS")
            return True
        elif (self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text()) and (
                self.buttons[0][2].text() != " "):
            print("THAT")
            return True

        for row in range(3):
            for button in range(3):
                if self.buttons[row][button] == self.sender():
                    if (self.buttons[row][button].text() == self.buttons[row - 1][button].text()
                        == self.buttons[row - 2][button].text()) and (self.buttons[row - 1][button].text() != " "):
                        return True
                    elif (self.buttons[row][button].text() == self.buttons[row][button - 1].text()
                          == self.buttons[row][button - 2].text()) and (self.buttons[row][button - 1].text() != " "):
                        return True
        return False


def window():
    app = QApplication(sys.argv)

    win = GUI()

    # Shows the GUI, it is like setting the visibility to true.
    win.show()
    # Makes sure that the app closes when pressing x.
    sys.exit(app.exec_())


window()
