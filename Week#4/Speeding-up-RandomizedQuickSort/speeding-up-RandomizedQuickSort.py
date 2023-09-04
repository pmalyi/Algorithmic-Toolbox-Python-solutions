from random import randint


def partition(A, low, high):
    pivot_index = randint(low, high)
    pivot = A[pivot_index]
    start = low
    end = high
    current = low
    while current <= end:
        if A[current] < pivot:
            A[current], A[start] = A[start], A[current]
            current += 1
            start +=1
        elif A[current] > pivot:
            A[current], A[end] = A[end], A[current]
            end -= 1
        else:
            current += 1
    return start, end


def randomizedQuickSort(A, low, high):
    if low < high:
        part1, part2 = partition(A, low, high)
        randomizedQuickSort(A, low, part1 - 1)
        randomizedQuickSort(A, part2 + 1, high)


n = int(input())
myList = list(map(int, input().split()[:n]))
randomizedQuickSort(myList, 0, n - 1)
print(*myList)