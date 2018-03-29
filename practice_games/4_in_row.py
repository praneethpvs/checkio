#!/usr/bin/env python
from pprint import pprint


class FourRow:
    def __init__(self, size):
        self.size = size
        self.board = None

    def initialize_board(self):
        self.board = [['-'] * self.size for _ in range(self.size)]

    def print_board(self):
        try:
            for row in self.board:
                for x in row:
                    print x,
                print ""
            print ""
        except Exception as e:
            pprint(e)

    def board_full(self):
        try:
            for row in self.board:
                if '-' in row:
                    return False
                else:
                    return True
        except Exception as e:
            pprint(e)

    def place_piece(self, position):
        try:
            for row in self.board[::-1]:
                if row[position] == '-':
                    row[position] = "x"
                    break
                return True
            else:
                pprint("The position {} is full. Please try an other one".format(position))
                return False
        except Exception as e:
            pprint(e)

    def ai(self):
        try:
            set_val = False
            for i in range((self.size - 1), -1, -1):
                for j in range(self.size):
                    if self.board[i][j] == '-':
                        self.board[i][j] = 'O'
                        set_val = True
                        break
                if set_val:
                    break
        except Exception as e:
            pprint(e)

    def check_row(self, user):
        try:
            for row in self.board:
                one_row = [str(1) if cell == user else str(0) for cell in row]
                row_str = ''.join(one_row)
                if '1111' in row_str:
                    break
            else:
                return False
            return True
        except Exception as e:
            pprint(e)

    def check_col(self, user):
        try:
            out_list = []
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[j][i] == user:
                        out_list.append(str(1))
                    else:
                        out_list.append(str(0))
                col_str = ''.join(out_list)
                if '1111' in col_str:
                    break
            else:
                return False
            return True
        except Exception as e:
            pprint(e)

    def check_diagonal(self, user):
        try:
            diagonal1 = [str(1) if self.board[i][i] == user else str(0) for i in range(self.size)]
            # pprint(diagonal1)
            diagonal2 = []
            i = self.size - 1
            j = 0
            while i >= 0 and j < self.size:
                if self.board[i][j] == user:
                    diagonal2.append(str(1))
                else:
                    diagonal2.append(str(0))
                j += 1
                i -= 1
            # pprint(diagonal2)
            if '1111' in ''.join(diagonal1) or '1111' in ''.join(diagonal2):
                return True
            else:
                return False
        except Exception as e:
            pprint(e)

    def check_won(self):
        try:
            bool_check = 0
            if self.check_row('x') or self.check_col('x') or self.check_diagonal('x'):
                pprint("User has won the game. ")
                bool_check = 1
                return True

            if self.check_row('O') or self.check_col('O') or self.check_diagonal('O'):
                pprint("Computer has won the game. ")
                bool_check = 1
                return True

            if bool_check == 0:
                return False
        except Exception as e:
            pprint(e)


if __name__ == "__main__":
    board_size = int(input("Enter the size of the n*n board: "))
    board = FourRow(board_size)
    board.initialize_board()
    board.print_board()
    while not board.board_full() or not board.check_won():
        while True:
            try:
                pos = int(input("Enter the position between 1 & {}: ".format(board_size)))
                if 1 <= pos <= board_size:
                    if board.place_piece(pos - 1):
                        board.print_board()
                        break
                else:
                    pprint("Please enter a valid input: ")
            except Exception as e:
                pprint(e)

        board.ai()
        board.print_board()
    else:
        pprint("Game is draw.")
# board = FourRow(5)
# board.initialize_board()
# board.place_piece(0)
# board.place_piece(1)
# board.place_piece(1)
# board.place_piece(2)
# board.place_piece(2)
# board.place_piece(2)
# board.place_piece(3)
# board.place_piece(3)
# board.place_piece(3)
# board.place_piece(3)
# board.print_board()
# pprint(board.check_diagonal('x'))
