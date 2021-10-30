from typing import List
import numpy as np
import copy

   
def calc(matrix , Ps):
    """ Calculates equation variables based on row reduced echeleon matrix.
    Replaces any free variable with 10.

    Parameters
    ----------
    matrix : numpy array
        Row reduced echeleon form of matrix
    Ps : list of tuples
        Pivot positions of the matrix
    """

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

def replace(matrix , row , byRow):
    """Performs the Replacement Row Function on a row by another row on the matrix.
    In this function (row) must be below (byRow). 

    Parameters
    ----------
    matrix: numpy array
        Given matrix
    row: list of numbers
        row to be replaces
    by row : list of numbers
        row to replace by
    """


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


def reverseReplace(matrix , row , byRow):
    """Performs the Replacement Row Function on a row by another row on the matrix.
    In this function (byRow) must be below (row).

    Parameters
    ----------
    matrix: numpy array
        Given matrix
    row: list of numbers
        row to be replaces
    by row : list of numbers
        row to replace by 
    """
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
    """Performs the Interchane Row Function.
    Parameters
    ----------
    matrix : numpy array
        Given matrix
    row : list of numbers
    withRow : list of numbers
    
    """
    # print("interchange:\n")

    tmp = copy.deepcopy(matrix[withRow])
    matrix[withRow] = matrix[row]
    matrix[row] = tmp
    # printUndecorated(matrix)
    return

def scaleToOne(matrix, row):
    """Performs the Scale Row Function by one.
    Scales the Given by the inverse of the first non-Zero entry.

    Parameters
    ----------
    matrix : np array
        Given matrix
    row : list of numbers
        row to scale
    """
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
    """ Creates zeros below a pivot point.

    Parameters
    ----------
    matrix: np array
        Given matrix
    PP : tuple
        Pivot Point
    """
    # print("zero down:\n")

    for y in range(PP[1] + 1 , matrix.shape[0]):
        if matrix[y, PP[0]] !=0:
            replace(matrix , y , PP[1])
    # printUndecorated(matrix)

def formEch(matrix):
    """Changes the matrix to an echeleon form. 
    Forward Phase.


    Parameters
    ----------
    matrix : np array
        Given Matrix
    
    Returns
    -------
    Ps : list of tuples
        Echeleon form pivot positions
    """
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
    """Row Reduces the Echeleon Form matrix.
    Backward Phase.
    
    Parameters
    ----------
    matrix: np array
        Given Matrix
    """
    # print("row reduce:\n")

    for i in reversed(range(0,matrix.shape[0])):
        scaleToOne(matrix, i)
        for j in reversed(range(0,i)):
            reverseReplace(matrix, j , i)
    roundElements(AugMat)
    # printUndecorated(matrix)



def roundElements(matrix):
    """ Rounds the all the elements of matrix by 3
    
    Parameters
    ----------
    matrix: np array
        Given Matrix
    """
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix[i,j] = round(matrix[i,j] , 3)


def calculateRow(P ,row):
    """ Calculates the constant variables of a row.
    Each pivot point represents a variable and replaces any other variables with nonzero coefficients to 10.
    
    Parameters
    ---------
    P: tuple
        Pivot Point
    row : list of numbers
        row of the pivot point
    
    Returns
    -------
    x : float
        value of variable xn
    """
    x = row[matSize[1]-1]
    for i in range(P[0]+1 , matSize[1] -1):
        x -= 10* row[i]
    return x

def inputMatrix(m , n):
    """Inputs a matrix frome console in the form of lines and changes it to matrix form.

    Parameters
    ----------
    m : int 
        number of rows
    n : int
        number of columns
    
    Returns
    -------
    matrix : np array
        matrix in the form of numpy array 
    """
    AugMatRows = []

    for i in range(m):
            AugMatRows = AugMatRows + list(map(float ,input().split()))

    return np.array(AugMatRows).reshape((m,n))

def printUndecorated(matrix):
    """ prints the numpy array without the bracets.

    Parameters
    ----------
    matrix: np array
        Given Matrix    
    """
    for i in matrix:
        print(' '.join(i.astype(str)))

#Initiate the matrix
matSize = list(map(int ,input().split()))

#Input the matrix from console
AugMat = inputMatrix(matSize[0] , matSize[1])

#Forward Phase
pivotPoints = formEch(AugMat)
#Backward Phase
rowReduce(AugMat)

#Output matrix
printUndecorated(AugMat)

#Calculate and output the answers
calc(AugMat, pivotPoints)

