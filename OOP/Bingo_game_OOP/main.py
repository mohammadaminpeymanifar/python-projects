import random

class Bingo_Game:
    player_list = []

    def __init__(self):
        self.name = input("Enter your name:")
        self.__rand_num = random.randint(0,10)
        self.__guess_left = 3
        self.__win_state = False
        self.player_list.append(self)

    def check_answer(self):

        try:
            answer = int(input(f"\n{self.name}. please enter your guess:"))
        except ValueError:
            print("Please enter a valid number")
            return

        if answer > self.__rand_num:
            print("Choose lower number")

        elif answer < self.__rand_num:
            print("Choose higher number")

        elif answer == self.__rand_num:
            print("Bingo!")
            self.__win_state = True
            return

        self.__minus_guess_left()
        print(f"{self.__guess_left} guesses left")

    def __minus_guess_left(self):
        self.__guess_left -= 1

    def has_guess_left(self):
        if self.__guess_left > 0:
            return True
        return False

    def has_won(self):
        return self.__win_state

    @classmethod
    def game_has_winner(cls):
        if any(Player.has_won() is True for Player in cls.player_list):
            return True
        return False

    @classmethod
    def all_players_lost(cls):
        if all(not player.has_guess_left() for player in cls.player_list):
            return True
        return False


class Game_Controller:
    def __init__(self):

        while True:

            for player in Bingo_Game.player_list:

                if player.has_guess_left() and not player.has_won():
                    player.check_answer()

                if Bingo_Game.game_has_winner():
                    print("Game Over")
                    return

            if Bingo_Game.all_players_lost():
                print("All players lost!")
                print("Game Over")
                return


if __name__ == "__main__":

    while True:

        order = input("What do you want to do?\nOrder:")

        if order == "add":
            Bingo_Game()

        elif order == "start":

            if len(Bingo_Game.player_list) == 0:
                print("No players added")
                continue

            Game_Controller()

        elif order == "exit":
            break

        else:
            print("Invalid order")