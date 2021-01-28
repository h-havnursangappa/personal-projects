import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_choice = False
        value = None
        while not valid_choice:
            square = input(self.letter + "\'s turn. Enter a value between (0-8): ")
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_choice = True
            except ValueError:
                print("Invalid input. Please enter a number between (0-8)")

        return value


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

