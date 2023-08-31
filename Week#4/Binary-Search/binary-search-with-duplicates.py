def binarySearch(A, low, high, key):
    result = -1
    while high >= low:
        middle = (low + high) // 2
        if A[middle] == key:
            result = middle
            break
        elif A[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    if result < 1 or A[result] != A[result - 1]:
        return result
    return binarySearch(A, low, result, key)


n = int(input())
sortedArr = tuple(map(int, input().split()[:n]))
m = int(input())
keys = tuple(map(int, input().split()[:m]))
for key in keys:
    result = binarySearch(sortedArr, 0, n - 1, key)
    print(result, end=' ')
