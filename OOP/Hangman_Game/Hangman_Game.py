import random

class Hangman:

    def __init__(self):
        self.words = [
            "python",
            "developer",
            "computer",
            "keyboard",
            "programming"
        ]

        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6

    def display_word(self):
        display = ""

        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        return display

    def play(self):

        print("Welcome to Hangman!")

        while self.attempts > 0:

            print("\nWord:", self.display_word())
            print("Remaining attempts:", self.attempts)

            guess = input("Enter a letter: ").lower()

            if guess in self.guessed_letters:
                print("You already guessed this letter!")
                continue

            self.guessed_letters.append(guess)

            if guess in self.secret_word:
                print("Correct!")
            else:
                self.attempts -= 1
                print("Wrong!")

            won = True

            for letter in self.secret_word:
                if letter not in self.guessed_letters:
                    won = False
                    break

            if won:
                print("\nCongratulations!")
                print("The word was:", self.secret_word)
                return

        print("\nGame Over!")
        print("The word was:", self.secret_word)


game = Hangman()
game.play()