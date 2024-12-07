def tukar(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubbleSortDistorted(A, n):
    if n == 1:
        return

    for i in range(n - 1):
        if (i % 2 == 0 and A[i] > A[i + 1]) or (i % 2 == 1 and A[i] < A[i + 1]):
            tukar(A, i, i + 1)

    bubbleSortDistorted(A, n - 1)

if __name__ == '__main__':
    A = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
    print("Sebelum Distorting:", A)

    bubbleSortDistorted(A, len(A))
    
    print("List yang sudah Distorting:\n", A)