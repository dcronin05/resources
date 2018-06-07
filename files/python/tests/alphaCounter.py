s = 'uzduwigs'

alpha = ''
lastLetter = s[:1]
substrings = ['']

for letter in s:
    if letter >= lastLetter:
        if len(substrings[-1:]) == 0:
            alpha += lastLetter

        # alpha += lastLetter
        # print('added', lastLetter, 'to alpha.')
        alpha += letter
        print('added', letter, 'to', alpha)
    # elif letter >= lastLetter:
    #     alpha += letter
    #     print('added', letter, 'to', alpha)
    else:
        alpha = ''
        print('no matches, cleared alpha.')

    substrings.append(alpha)
    print('added', alpha, 'to substrings:\n', substrings)
    lastLetter = letter
    print('changed lastLetter to', letter)

score = 0
winner = []

for string in substrings:
    if len(string) > score:
        score = len(string)
        winner = [string]

print('Longest substring in alphabetical order is:', *winner)