s = 'skhgbobuahsdksahfdjkbobaslkjdhfalskhdfbobsldkfsklhf'


indexStart = 0
indexEnd = 3
bobCount = 0

while True:
    if s[indexStart:indexEnd] == 'bob':
        bobCount += 1
    indexStart += 1
    indexEnd += 1
    if indexEnd > len(s):
        break

print('Bob count is:', bobCount)