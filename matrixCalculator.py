import numpy as np


def addMatrices(A, B):
    return A + B


def subtractMatrices(A, B):
    return A - B


def multiplyMatrices(A, B):
    return np.dot(A, B)


def determinantMatrix(A):
    return np.linalg.det(A)


def inverseMatrix(A):
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



def main():
    print("=== MATRIX CALCULATOR ===")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Determinant")
    print("5. Inverse")
    print("0. Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("Exiting... Bye!")
            break

        elif choice in ["1", "2", "3"]:
            A = getMatrix("A")
            B = getMatrix("B")
            try:
                if choice == "1":
                    print("\nResult:\n", addMatrices(A, B))
                elif choice == "2":
                    print("\nResult:\n", subtractMatrices(A, B))
                elif choice == "3":
                    print("\nResult:\n", multiplyMatrices(A, B))
            except ValueError as e:
                print("Error:", e)

        elif choice == "4":
            A = getMatrix("A")
            # Check if the matrix is a square matrix
            if A.shape[0] == A.shape[1]:
                print("\nDeterminant =", determinantMatrix(A))
            else:
                print("Determinant can only be found for square matrices.")

        elif choice == "5":
            A = getMatrix("A")
            # Check if the matrix is a square matrix
            if A.shape[0] == A.shape[1]:
                try:
                    print("\nInverse:\n", inverseMatrix(A))
                except np.linalg.LinAlgError:
                    print("Matrix is singular (no inverse).")
            else:
                print("Inverse can only be found for square matrices.")
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()


