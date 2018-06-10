high = 100
low = 0
num = 50


def average(high, low):
    num = int((high + low) / 2)
    return num


print("Please think of a number between 0 and 100!")


while True:
    print("Is your secret number %s?" % num)
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user == 'h':
        high = num
        num = average(high, low)
    if user == 'l':
        low = num
        num = average(high, low)
    if user == 'c':
        print("Game over. Your secret number was: %s" % num)
        break



# class Guess:
#
#     def __init__(self):
#         self.high = 100
#         self.input = ''
#         self.low = 0
#         self.average()
#         self.hint()
#         self.bisect()
#
#     def average(self):
#         self.ans = (self.high + self.low) / 2
#
#     def bisect(self):
#         while True:
#             if self.input == 'c':
#                 print("Game over. Your secret number was: %s" % self.ans)
#                 exit()
#             elif self.input == 'h':
#                 self.high = self.ans
#                 self.average()
#                 self.hint()
#             elif self.input == 'l':
#                 self.low = self.ans
#                 self.average()
#                 self.hint()
#             else:
#                 print("Sorry, I did not understand your input.")
#                 self.hint()
#
#     def hint(self):
#         print("Is your secret number %s?" % round(self.ans))
#         self.input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n")
#
# print("Please think of a number between 0 and 100!")
# guess = Guess()
