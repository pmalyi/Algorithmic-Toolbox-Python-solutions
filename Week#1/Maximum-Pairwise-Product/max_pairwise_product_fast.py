def maxPairwiseProductFast(A):
    max_n = 0
    second_max = 0
    for i in range(len(A)):
        if A[i] > second_max:
            second_max = A[i]
            if second_max >= max_n:
                max_n, second_max = second_max, max_n
    return second_max * max_n
