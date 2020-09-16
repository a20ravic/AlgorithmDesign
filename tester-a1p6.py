#! /usr/bin/python3

import sys
import random
from a1p6 import sformbnine

"""
Some tests.

If you set this file to executable, and have the a1p6.py file in
the same folder, then you should be able to run this.
"""

def main():
    print('Test 1:', end = ' ')
    failure = False
    ret = sformbnine([1,1])

    if((not isinstance(ret,list)) or len(ret) != 2):
        failure = True
    elif(ret[0] != 1 or ret[1] != 1):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 2:', end = ' ')
    failure = False
    ret = sformbnine([11,27])

    if((not isinstance(ret,list)) or len(ret) != 2):
        failure = True
    elif(ret[0] != 2 or ret[1] != 5):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 3:', end = ' ')
    failure = False
    ret = sformbnine([14,35])

    if((not isinstance(ret,list)) or len(ret) != 2):
        failure = True
    elif(ret[0] != 14 or ret[1] != 35):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 4:', end = ' ')
    failure = False
    N = [2,4,8]
    D = [1,3,5,7]
    n = N[random.randint(0,len(N)-1)]
    d = D[random.randint(0,len(D)-1)]
    ret = sformbnine([n,d])

    if((not isinstance(ret,list)) or len(ret) != 2):
        failure = True
    elif(ret[0] != n or ret[1] != d):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

if __name__ == '__main__':
    main()
