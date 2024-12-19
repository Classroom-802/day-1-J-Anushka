import numpy as np

# Function for matrix addition
def operate(A, B, operation):
    if operation == 1:  
        if A.shape == B.shape:
            result = A + B
            return result
        else:
            return "Invalid dimensions for operation."
    
    elif operation == 2:  
        
        if A.shape[1] == B.shape[0]:
            result = np.dot(A, B)
            return result
        else:
            return "Invalid dimensions for operation."
    else:
        return "Invalid operation."

# Input: Read matrix A and matrix B
m, n = map(int, input().split())  
Matrix_A = []
for _ in range(m):
    row = list(map(int, input().split()))
    Matrix_A.append(row)

n, p = map(int, input().split())  
Matrix_B = []
for _ in range(n):
    row = list(map(int, input().split()))
    Matrix_B.append(row)

# Convert matrices to numpy arrays
Matrix_A = np.array(Matrix_A)
Matrix_B = np.array(Matrix_B)

# Input: Operation type
operation = int(input())

# Call the function to perform the operation
result = operate(Matrix_A, Matrix_B, operation)

# Output the result
if isinstance(result, str):  
    print(result)
else:
    for row in result:
        print(" ".join(map(str, row)))
