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
        x = (matrix[row][nonZero] / matrix[byRow][nonZero]) * -1
    
    for i in range(nonZero , matrix.shape[1]):
        matrix[row][i] = matrix[row][i] + (matrix[byRow][i] * x)
    
    return

def interchange(matrix, row , withRow):
    tmp = copy.deepcopy(matrix[withRow])
    matrix[withRow] = matrix[row]
    matrix[row] = tmp
    return

def scaleToOne(matrix, row):
    n =  0
    while(matrix[row , n] == 0):
        n+=1
    times = 1 / matrix[row,n]
    matrix[row] = [x * times for x in matrix[row]]
    return

def zeroBelow(matrix , PP):
    for y in range(PP[1] + 1 , matrix.shape[0]):
        if matrix[y, PP[0]] !=0:
            replace(matrix , y , PP[1])

def formEch(matrix):

    Px = 0
    Py = 0
    Ps = []

    while(Px < matSize[1] and Py < matSize[0]):
        
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
    for i in reversed(range(0,matrix.shape[0])):
        scaleToOne(matrix, i)
        for j in reversed(range(0,i)):
            replace(matrix , j , i)
    roundElements(AugMat)



def roundElements(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix[i,j] = round(matrix[i,j] , 3)


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
rowReduce(AugMat)


printUndecorated(AugMat)

print(pivotPoints)