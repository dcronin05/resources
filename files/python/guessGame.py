# !/usr/bin/python3


class Guess:

    def __init__(self):
        self.guess = input("Please think of a number between 0 and 100!")


newGuess = Guess(input(""))

newGuess.input_guess()

print(newGuess.guess)
# print(Guess.guess)
