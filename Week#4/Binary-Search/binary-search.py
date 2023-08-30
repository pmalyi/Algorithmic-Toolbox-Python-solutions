def binarySearch(A, key):
    low = 0
    high = len(A) - 1
    while high >= low:
        middle = (low + high) // 2
        if A[middle] == key:
            return middle
        if A[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    return -1


n = int(input())
sortedArr = tuple(map(int, input().split()[:n]))
m = int(input())
keys = tuple(map(int, input().split()[:m]))
for key in keys:
    result = binarySearch(sortedArr, key)
    print(result, end=' ')
