from typing import List
import numpy as np
import copy

def calc(matrix):
    pass

def replace(matrix , row , byRow):

    x = 0

    if(matrix[byRow][0] != 0):
        x = (matrix[row][0] / matrix[byRow][0]) * -1
        print(x)
    
    for i in range(matrix.shape[1]):
        matrix[row][i] = matrix[row][i] + (matrix[byRow][i] * x)
    
    return

def interchange(matrix, row , withRow):
    tmp = copy.deepcopy(matrix[withRow])
    matrix[withRow] = matrix[row]
    matrix[row] = tmp
    return

def scale(matrix, row , times):
    matrix[row] = [x * times for x in matrix[row]]
    return


def rowReduce(matrix):
    pass

def inputMatrix(m , n):
    AugMatRows = []

    for i in range(m):
            AugMatRows = AugMatRows + list(map(float ,input().split()))

    return np.array(AugMatRows).reshape((m,n))

def printUndecorated(matrix):
    for i in matrix:
        print(' '.join(i.astype(str)))


matSize = list(map(int ,input().split()))
AugMat = inputMatrix(matSize[0] , matSize[1])

printUndecorated(AugMat)