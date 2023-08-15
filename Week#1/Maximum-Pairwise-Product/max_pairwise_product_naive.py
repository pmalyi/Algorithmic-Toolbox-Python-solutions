def maxPairwiseProductNaive(A):
    n = len(A)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] * A[j] > result:
                result = A[i] * A[j]
    return result