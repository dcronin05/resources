def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
        that f(s) returns True, and no other elements. Remaining elements in L
        should be in the same order.
    Returns the length of L after mutation
    """

    adj = 0

    while True:
        if len(L) == adj:
            break

        for i in range(adj, len(L), 1):
            if not f(L[i]):
                L.pop(adj)
                break
            else:
                adj += 1
                break

    return len(L)


def f(s):
    return 'abc' in s


L = ['a', 'b', 'abc', 'e', 'f', 'abceafd', 'a', 'ac', 'abca', 'a', 'c', 'd', 'e']
print(satisfiesF(L))
print(L)