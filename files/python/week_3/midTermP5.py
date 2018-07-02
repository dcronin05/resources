def keysWithValue(aDict, target):

    answer = []

    for i in aDict:
        if aDict[i] == target:
            answer.append(i)

    return answer

print(keysWithValue({1: 1, 2: 0, 3: 4, 4: 1, 5: 2, 7: 0, 8: 4, 9: 1, 10: 1}, 1))