def bin_search_rec(A, key, left, right):
    if left > right:
        return "not found"
    middle = (left + right) // 2
    if key == A[middle]:
        return middle
    if key < A[middle]:
        return bin_search_rec(A, key, left, middle - 1)
    else:
        return bin_search_rec(A, key, middle + 1, left)


if __name__ == "__main__":
    key = input()
    A = input().split()  # input sorted array
    print(bin_search_rec(A, key, 0, len(A) - 1))