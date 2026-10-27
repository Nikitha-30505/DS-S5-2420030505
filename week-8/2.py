# QR Decomposition using Gram-Schmidt Method
# Application: Solving Linear System Ax = b

import numpy as np
def qr_decomposition(A):
    n = A.shape[0]
    # Initialize Q and R matrices
    Q = np.zeros((n, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return Q, R
def solve_qr(Q, R, b):
    # Compute Qᵀb
    y = np.dot(Q.T, b)
    # Backward substitution to solve Rx = y
    n = R.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_value = 0
        for j in range(i + 1, n):
            sum_value += R[i, j] * x[j]

        x[i] = (y[i] - sum_value) / R[i, i]
    return x
# Input Matrix A
A = np.array([
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
], dtype=float)
# Constant Matrix b
b = np.array([4, 5, 6], dtype=float)
# Perform QR Decomposition
Q, R = qr_decomposition(A)
# Solve system using QR decomposition
x = solve_qr(Q, R, b)
# Display Results
print("Matrix A:")
print(A)
print("\nOrthogonal Matrix Q:")
print(Q)
print("\nUpper Triangular Matrix R:")
print(R)
print("\nSolution Vector x:")
print(x)
