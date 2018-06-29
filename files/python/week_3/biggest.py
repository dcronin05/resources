def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here

    answer = ''
    result = {}
    for big in aDict:
        if len(aDict[big]) != 0:
            result[big] = len(aDict[big])
    best = max(result.values())
    for i in result:
        if result[i] < best:
            del result[i]
    for i in result.keys():
        answer = answer + i
    return answer


print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))
