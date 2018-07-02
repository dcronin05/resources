def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''

    answer = 0

    for i in range(len(listA)):
        answer += listA[i] * listB[i]

    return answer

print(dotProduct([-85, -69, -6, -51, 27, -73, 48, -17], [89, 86, 57, 47, -45, -81, -3, 64]))