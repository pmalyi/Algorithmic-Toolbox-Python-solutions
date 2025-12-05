def bin_search(A, key, left, right):
    while left <= right:
        middle = (left + right) // 2
        if key == A[middle]:
            return middle
        if key < A[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return "not found"

if __name__ == "__main__":
    key = input()
    A = input().split()  # input sorted array
    print(bin_search(A, key, 0, len(A) - 1))