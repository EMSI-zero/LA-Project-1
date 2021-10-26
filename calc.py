from typing import List
import numpy as np

def calc(matrix):
    pass

def replace(matrix , row , byRow):
    pass

def interchange(matrix, row , byRow):
    pass

def scale(matrix, row , times):
    pass


def rowReduce(matrix):
    pass

def inputMatrix(m , n):
    AugMatRows = []

    for i in range(m):
            AugMatRows = AugMatRows + list(map(int ,input().split()))

    return np.array(AugMatRows).reshape((m,n))

def printUndecorated(matrix):
    for i in matrix:
        print(' '.join(i.astype(str)))

