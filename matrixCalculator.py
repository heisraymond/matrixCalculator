import numpy as np


def addMatrices(A, B):
    return A + B


def subtractMatrices(A, B):
    return A - B


def multiplyMatrices(A, B):
    return np.dot(A, B)


def determinantMarix(A, B):
    return np.linalg.det()


def inverseMatrix(A, B):
    return np.linalg.inv(A)


def getMatrix(name):
    print(f"\nEnter the size of the Matrix {name} (rows columns): ", end="")
    rows, cols = map(int, input().split())
    print(f"Enter the elements of Matrix {name} row by row (space separated):")
    
    elements = []
    for i in range(rows):
        while True:
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            
            if len(row) != cols:
                print(f"You must enter exactly {cols} numbers. Try again.")
                continue
            
            elements.append(row)
            break  
    
    return np.array(elements)
