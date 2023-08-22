def isBetter(s1, s2):
    res1 = int(s1 + s2)
    res2 = int(s2 + s1)
    if res1 >= res2:
        return True
    return False


def partition(A, low, high):
    partition_index = (low - 1)
    pivot = A[high]
    for current_index in range(low, high):
        if isBetter(A[current_index],pivot):
            partition_index += 1
            A[partition_index], A[current_index] = A[current_index], A[partition_index]
    partition_index += 1
    A[partition_index], A[high] = A[high], A[partition_index]
    return partition_index


def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)


n = int(input())
yourSalary = list(map(str, input().split()))
quicksort(yourSalary, 0, n - 1)
print(*yourSalary, sep='')
