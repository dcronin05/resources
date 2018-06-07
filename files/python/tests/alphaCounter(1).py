s = 'zyxwvutsrqponmlkjihgfedcba'

counter = 1
alpha = s[counter-1:counter]
winner = alpha

for letter in s:
    if s[counter:counter+1] >= letter:
        if len(alpha) == 0:
            alpha = letter + s[counter:counter+1]
        else:
            alpha += s[counter:counter+1]
    else:
        alpha = ''

    if len(winner) < len(alpha):
        winner = alpha

    counter += 1


print("Longest substring in alphabetical order is: {0}".format(winner))
