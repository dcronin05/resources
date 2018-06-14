class Guess:

    def __init__(self):
        self.high = 100
        self.low = 0
        self.average()
        self.hint()
        self.bisect()

    def average(self):
        self.ans = (self.high + self.low) / 2

    def bisect(self):
        while True:
            if self.input == 'c':
                print("Game over. Your secret number was: %s" % self.ans)
                exit()
            elif self.input == 'h':
                self.high = self.ans
                self.average()
                self.hint()
            elif self.input == 'l':
                self.low = self.ans
                self.average()
                self.hint()
            else:
                print("Sorry, I did not understand your input.")
                self.hint()

    def hint(self):
        print("Is your secret number %s?" % round(self.ans))
        self.input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n")


guess = Guess()
