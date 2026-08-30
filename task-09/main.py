import time
import random

def naive(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def divide_conquer(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    #splitting the matrix
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    C11 = add(divide_conquer(A11, B11),
              divide_conquer(A12, B21))

    C12 = add(divide_conquer(A11, B12),
              divide_conquer(A12, B22))

    C21 = add(divide_conquer(A21, B11),
              divide_conquer(A22, B21))

    C22 = add(divide_conquer(A21, B12),
              divide_conquer(A22, B22))

    return combine(C11, C12, C21, C22)

def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    return combine(C11, C12, C21, C22)

def combine(A, B, C, D):
    top = [A[i] + B[i] for i in range(len(A))]
    bottom = [C[i] + D[i] for i in range(len(C))]
    return top + bottom

def pad(A, size):
    n = len(A)
    return [
        [A[i][j] if i < n and j < n else 0
         for j in range(size)]
        for i in range(size)
    ]


def next_power_of_2(n):
    size = 1
    while size < n:
        size *= 2
    return size

def same(A, B):
    return A == B

n = int(input("Enter matrix size n: "))

A = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
B = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

print("\nMatrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)


# Naive
start = time.perf_counter()
C1 = naive(A, B)
t1 = time.perf_counter() - start


# Divide and Conquer
size = next_power_of_2(n)
A2 = pad(A, size)
B2 = pad(B, size)

start = time.perf_counter()
C2 = divide_conquer(A2, B2)
t2 = time.perf_counter() - start

C2 = [row[:n] for row in C2[:n]]


# Strassen
start = time.perf_counter()
C3 = strassen(A2, B2)
t3 = time.perf_counter() - start

C3 = [row[:n] for row in C3[:n]]


# Results
print("\nTime Taken:")
print("Naive           :", round(t1 * 1000, 3), "ms")
print("Divide & Conquer:", round(t2 * 1000, 3), "ms")
print("Strassen        :", round(t3 * 1000, 3), "ms")

print("\nVerification:")
if same(C1, C2) and same(C1, C3):
    print("PASSED")
else:
    print("FAILED")

print("\nResult Matrix:")
for row in C1:
    print(row)