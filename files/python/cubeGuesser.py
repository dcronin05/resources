cube = 300
epsilon = 0.0001
guess = 0
increment = 0.00001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
    # print(guess)
    if guess**3 >= (cube + 1):
        break

print('num_guesses =',num_guesses)
print('guess =', guess)
print('guess**3 =', guess**3)
print('difference =', (guess**3 - cube))

if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)