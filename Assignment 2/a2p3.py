"""
ECE606, F'20, Assignment 2, Problem 3
Skeleton solution file
"""

"""
You are not allowed to import anything
"""

all_alphabets = True


def vocab(char, all_alphabets=True):
    if all_alphabets:
        position = ord(char) - ord("a")
        return position
    vocab = {"a": 0, "b": 1, "d": 2}
    return vocab[char]


def makeNode(T, all_alphabets=True):
    vocab_length = 26 if all_alphabets else 3
    for _ in range(0, vocab_length):
        T.append([[], False])


def InsertIntoTrie(T, s):
    """
    You need to implement this method.
    You are certainly allowed to define any subroutines you want
    above this method in this file.
    """
    insert_position = vocab(s[0], all_alphabets)
    if T == []:
        makeNode(T, all_alphabets)
    if s[1:] == "":
        T[insert_position][1] = True
    else:
        InsertIntoTrie(T[insert_position][0], s[1:])


def cleanUpLevel(T, all_alphabets=True):
    # print(T)
    vocab_length = 26 if all_alphabets else 3
    for i in range(0, vocab_length):
        _branch, _end = T[i][0], T[i][1]
        if _branch != [] or _end != False:
            return
    T.clear()


def DeleteFromTrie(T, s):
    """
    You need to implement this method.
    You are certainly allowed to define any subroutines you want
    above this method in this file.
    """
    if T == [] or len(s) == 0:
        return
    position = vocab(s[0], all_alphabets)
    if len(s) == 1:
        # string ends, check and clear and return
        T[position][1] = False
        cleanUpLevel(T, all_alphabets)
        return
    if T[position][0] != []:
        DeleteFromTrie(T[position][0], s[1:])
        cleanUpLevel(T, all_alphabets)