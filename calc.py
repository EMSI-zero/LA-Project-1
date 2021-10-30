from typing import List
import numpy as np
import copy

def calc(matrix , Ps):
    # print("calc:\n")
    Px = 0
    Py = 0
    while(Px < matrix.shape[1] -1):
        if (Px , Py) not in Ps:
            print("X" + str(Px+1) + " = 10")
            Px += 1
        else:
            x = calculateRow((Px , Py) , matrix[Py])
            print("X" + str(Px+1) + " = " + str(x))
            Px+=1
            if Py !=  matrix.shape[0] -1:
                Py+=1
    # printUndecorated(matrix)
    pass

def replace(matrix , row , byRow):
    # print("replace:\n")

    x = 0
    nonZero = 0
    while(matrix[row][nonZero]== 0 and nonZero< matrix.shape[1]):
        nonZero += 1
    if(matrix[byRow][nonZero] != 0):
        x = (matrix[row][nonZero] / matrix[byRow][nonZero]) * -1
    else:
        pass
    for i in range(nonZero , matrix.shape[1]):
        matrix[row][i] = matrix[row][i] + (matrix[byRow][i] * x)
    # printUndecorated(matrix)
    return

def reverseReplace(matrix , row , byRow):
    # print("reverse replace:\n")

    x = 0
    nonZero = 0
    while(matrix[byRow][nonZero]== 0 and nonZero< matrix.shape[1]-1):
        nonZero += 1
    if(matrix[byRow][nonZero] != 0):
        x = (matrix[row][nonZero] / matrix[byRow][nonZero]) * -1
    else:
        pass
    for i in range(nonZero , matrix.shape[1]):
        matrix[row][i] = matrix[row][i] + (matrix[byRow][i] * x)
    # printUndecorated(matrix)
    return

def interchange(matrix, row , withRow):
    # print("interchange:\n")

    tmp = copy.deepcopy(matrix[withRow])
    matrix[withRow] = matrix[row]
    matrix[row] = tmp
    # printUndecorated(matrix)
    return

def scaleToOne(matrix, row):
    # print("scale:\n")
    n =  0
    # print("row"+str(row))
    while(matrix[row , n] == 0 and n < matrix.shape[1]-1):
        n+=1
        print(str(n))
    # printUndecorated(matrix)
    times = 0
    if matrix[row,n] !=0:    
        times = 1 / matrix[row,n]
    matrix[row] = [x * times for x in matrix[row]]
    return

def zeroBelow(matrix , PP):
    # print("zero down:\n")

    for y in range(PP[1] + 1 , matrix.shape[0]):
        if matrix[y, PP[0]] !=0:
            replace(matrix , y , PP[1])
    # printUndecorated(matrix)

def formEch(matrix):
    # print("form echeleon:\n")

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
    # printUndecorated(matrix)
    return Ps



def rowReduce(matrix):
    # print("row reduce:\n")

    for i in reversed(range(0,matrix.shape[0])):
        scaleToOne(matrix, i)
        for j in reversed(range(0,i)):
            reverseReplace(matrix, j , i)
    roundElements(AugMat)
    # printUndecorated(matrix)



def roundElements(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix[i,j] = round(matrix[i,j] , 3)


def calculateRow(P ,row):
    x = row[matSize[1]-1]
    for i in range(P[0]+1 , matSize[1] -1):
        x -= 10* row[i]
    return x

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

calc(AugMat, pivotPoints)

