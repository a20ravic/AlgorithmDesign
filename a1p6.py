"""
ECE606, F'20, Assignment 1, Problem 6
Skeleton solution file.
"""

"""
You are not allowed to import anything
"""

def gcd(n, d):
    while d != 0:
        (n, d) = (d, n % d)
    return n


def from_baseN(n, from_base=9):
    output, i = 0, 0
    while n > 0:
        r = n % 10
        n = n // 10
        output += r * (from_base ** i)
        i += 1
    return output


def to_baseN(n, to_base=9):
    output = ""
    while n > 0:
        r = n % to_base
        n = n // to_base
        output = str(r) + output
    return int(output)

def sformbnine(items):
    """
    You need to implement this method.
    You are certainly allowed to define any subroutines you want
    above this method in this file.
    """
    n, d = items[0], items[1]
    n, d = from_baseN(n, 9), from_baseN(d, 9)

    # print(n, d)

    gcd_n = gcd(n, d)

    # print(gcd_n)

    n, d = n // gcd_n, d // gcd_n

    # print(n, d)

    return [to_baseN(n, 9), to_baseN(d, 9)]