from player import HumanPlayer, ComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[ii*3:(ii+1)*3] for ii in range(3)]:
            print("|" + "|".join(row) + "|")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("|" + "|".join(row) + "|")

    def available_moves(self):
        moves = [idx for idx, spot in enumerate(self.board) if spot == " "]
        # for idx, spot in enumerate(self.board):
        #     if spot == " ":
        #         moves.append(idx)
        return moves

    def winner(self, letter, square):
        # Check row
        row_idx = square // 3
        row = self.board[row_idx*3:row_idx+1*3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_idx = square % 3
        col = [self.board[col_idx+ii*3] for ii in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # Check Diagonals
        diagonal1 = [self.board[idx] for idx in [0, 4, 8]]
        if all([spot == letter for spot in diagonal1]):
            return True
        diagonal2 = [self.board[idx] for idx in [2, 4, 6]]
        if all([spot == letter for spot in diagonal2]):
            return True

        return False

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter

            # Check for winner
            if self.winner(letter, square):
                self.current_winner = letter
            return True
        return False


def play(game, x_player, o_player, print_board=True):

    letter = "X"
    if print_board:
        game.print_board_nums()

    while " " in game.board:
        if letter == "X":
            square = x_player.get_move(game)
        else:
            time.sleep(1)
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_board:
                print(f'{letter} makes a move to index {square}')
                game.print_board()
                print(" ")

            if game.current_winner:
                print(letter + " wins !")
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_board:
        print("It's a tie")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_board=True)
