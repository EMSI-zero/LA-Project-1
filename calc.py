from typing import List
import numpy as np
import copy

def calc(matrix):
    pass

def replace(matrix , row , byRow):

    x = 0
    nonZero = 0
    while(matrix[row][nonZero] * matrix[byRow][nonZero] == 0):
        nonZero += 1

    if(matrix[byRow][nonZero] != 0):
        x = round((matrix[row][nonZero] / matrix[byRow][nonZero]) * -1 , 3)
        print('x=', x)
    
    for i in range(nonZero , matrix.shape[1]):
        matrix[row][i] = round(matrix[row][i] + (matrix[byRow][i] * x),2)
    
    return

def interchange(matrix, row , withRow):
    print('interchange')
    tmp = copy.deepcopy(matrix[withRow])
    matrix[withRow] = matrix[row]
    matrix[row] = tmp
    return

def scale(matrix, row , times):
    matrix[row] = [x * times for x in matrix[row]]
    return

def zeroBelow(matrix , PP):
    for y in range(PP[1] + 1 , matrix.shape[0]):
        print('form pivot', y , PP[1])
        printUndecorated(matrix)
        if matrix[y, PP[0]] !=0:
            replace(matrix , y , PP[1])

def formEch(matrix):

    Px = 0
    Py = 0
    Ps = []

    while(Px < matSize[1] and Py < matSize[0]):
        print('++')
        printUndecorated(AugMat)
        print(Ps)
        if (AugMat[Py][Px] == 0):
            for y in range(Py , matSize[1]):
                if (y<matSize[0] and Px < matSize[1]):
                    if  AugMat[y][Px] != 0:
                        interchange(AugMat , Py , y)
                        Ps.append((Px , Py))
                        zeroBelow(AugMat , (Px,Py))
                        Px+=1
                        Py+=1
                        break
            else:
                Px+=1
        else:
            Ps.append((Px , Py))
            zeroBelow(AugMat , (Px,Py))
            Px+=1
            Py+=1
    return Ps



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

pivotPoints = formEch(AugMat)



printUndecorated(AugMat)

print(pivotPoints)