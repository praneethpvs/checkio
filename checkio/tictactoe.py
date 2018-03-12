#!/usr/bin/env python
from pprint import pprint


class TicTacToe():
    def __init__(self):
        self.board = ['-'] * 9
        self.count = 0
        self.winning_sequence = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

    def printboard(self):
        count = 0
        try:
            for x in self.board:
                print x,
                count += 1
                if count % 3 != 0:
                    print "|",
                else:
                    print ""
            print ""
        except Exception as e:
            pprint(e)

    def checkempty(self, pos):
        try:
            if self.board[pos] == '-':
                return True
            else:
                pprint("The entered position is not empty. Please choose an other position.")
                return False
        except Exception as e:
            pprint(e)

    @property
    def boardfull(self):
        try:
            if '-' in self.board:
                return False
            else:
                return True
        except Exception as e:
            pprint(e)

    @staticmethod
    def listrange(pos):
        try:
            if 0 <= pos < 9:
                return True
            else:
                pprint("specified position value is out of range.")
                return False
        except Exception as e:
            pprint(e)

    def addtoken(self, pos, token):
        try:
            if self.listrange(pos) and self.checkempty(pos):
                self.board[pos] = token
                self.count += 1
                return True
            else:
                return False
        except Exception as e:
            pprint(e)

    def ai(self):
        try:
            for val in self.board:
                if val == '-':
                    self.board[self.board.index('-')] = 'O'
                    break
        except Exception as e:
            pprint(e)

    def game_won(self):
        try:
            for sequence in self.winning_sequence:
                if self.board[sequence[0]] == self.board[sequence[1]] == self.board[sequence[2]] == 'X':
                    pprint("User has won the game")
                    return True
                elif self.board[sequence[0]] == self.board[sequence[1]] == self.board[sequence[2]] == 'O':
                    pprint("Computer has won the game")
                    return True
            else:
                return False
        except Exception as e:
            pprint(e)


if __name__ == "__main__":
    board = TicTacToe()
    board.printboard()
    while not board.game_won() and not board.boardfull:
        while True:
            position = raw_input("Enter a value ranging between 0 to 8: ")
            if board.addtoken(int(position), 'X'):
                break
        board.printboard()
        board.ai()
        board.printboard()
