import numpy as np

def strassen(A, B):
    # Base case for 1x1 matrix
    if A.shape == (1, 1):
        return A * B

    n = A.shape[0]  # Since A and B are guaranteed to be 2^k x 2^k
    mid = n // 2

    # Split matrices into quadrants
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    # Strassen's algorithm formula
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # Combine results into the final matrix
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Assemble the final result
    C = np.zeros((n, n), dtype=A.dtype)
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C


msize = 128  # matrix size
low = 0  # Minimum value 
high = 25  # Maximum value 
matrixa = np.random.randint(low, high, size=(msize, msize))
matrixb = np.random.randint(low, high, size=(msize, msize))

C_s = strassen(matrixa, matrixb)
C_p = matrixa @ matrixb
E = C_s - C_p

frobenius_norm = np.sqrt(np.sum(E**2))

if np.all(E == 0):
    print("There is no discrepancy; C_s and C_p are equal.")
else:
    print("There is a discrepancy.")


print (f"forbeniusnorm = {frobenius_norm}")

# Compute the Frobenius norm of C_s
frobenius_norm_C = np.sqrt(np.sum(C_s**2))

# Calculate the relative error
RE = frobenius_norm / frobenius_norm_C

# Output the relative error
print("Relative Error (RE):", RE)
