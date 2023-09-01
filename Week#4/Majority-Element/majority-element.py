def partition(A, low, high):
    pivot = A[low]
    partition = 0
    count_pivot = 1
    for current in range(low + 1, high + 1):
        if A[current] == pivot:
            count_pivot += 1
        if A[current] < pivot:
            partition += 1
            A[current], A[partition] = A[partition], A[current]
    A[low], A[partition] = A[partition], A[low]
    return partition, count_pivot


def majorityElement(A, low, high, n):
    part, count_pivot = partition(A, low, high)
    if count_pivot > n // 2:
        return 1
    if part - low > high - part - count_pivot + 1:
        high = part - 1
    else:
        low = part + count_pivot
    if high - low < n // 2:
        return 0
    return majorityElement(A, low, high, n)


n = int(input())
A = list(map(int, input().split()[:n]))
print(majorityElement(A, 0, n - 1, n))
# print(A)
