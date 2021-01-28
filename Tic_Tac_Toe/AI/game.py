from player import HumanPlayer, ComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for ii in range(3):
            row = self.board[ii*3:(ii+1)*3]
            print('| ' + ' | '.join(row) + ' |')

        # for row in [self.board[ii*3:ii+1*3] for ii in range(3)]:
        #     print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        board_nums = [[str(jj) for jj in range(kk*3, (kk+1)*3)] for kk in range(3)]
        for row in board_nums:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [idx for idx, space in enumerate(self.board) if space == " "]

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())

    def winner(self, square, letter):
        # Check row
        row_idx = square // 3
        row = self.board[row_idx*3:(row_idx+1)*3]
        if all([space == letter for space in row]):
            return True

        # Check collumn
        col_idx = square % 3
        column = [self.board[col_idx+ii*3] for ii in range(3)]
        if all([space == letter for space in column]):
            return True

        # Check diagonals
        diag1 = [self.board[mm] for mm in [0, 4, 8]]
        if all([space == letter for space in diag1]):
            return True

        diag2 = [self.board[nn] for nn in [2, 4, 6]]
        if all([space == letter for space in diag2]):
            return True

        return False

    def make_move(self, spot, letter):
        if self.board[spot] == " ":
            self.board[spot] = letter
            if self.winner(spot, letter):
                self.current_winner = True
            return True
        return False

def play(game, x_player, o_player):
    game.print_board_nums()
    letter = 'X'

    while game.empty_squares():
        if letter == 'X':
            move = x_player.get_move(game)
        else:
            move = o_player.get_move(game)

        if game.make_move(move, letter):
            game.print_board(git)
            print(f"{letter} made a move to square {move}")
            print('\n')

            if game.current_winner:
                print(f"{letter} wins!")
                return letter

        letter = 'O' if letter == 'X' else 'X'
        time.sleep(1)

    print("It's a Tie")


if __name__ == '__main__':
    t = TicTacToe()
    x = HumanPlayer('X')
    # o = ComputerPlayer('O')
    o = GeniusComputerPlayer('O')
    play(t, x, o)





