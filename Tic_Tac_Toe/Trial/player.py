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
        place = None
        while not valid_choice:
            move = input(self.letter + "'s turn " + "Enter a number in the range (0-8): ")
            try:
                place = int(move)
                if place not in game.available_moves():
                    raise ValueError
                valid_choice = True
            except ValueError:
                print("Invalid Choice! Try again")

        return place


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move = random.choice(game.available_moves())
        return int(move)