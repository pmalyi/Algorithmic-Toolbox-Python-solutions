def line_search_rec(A, key, low, high):
    if low > high:
        return "not found"
    if key == A[low]:
        return low
    return line_search_rec(A, key, low + 1, high)


if __name__ == "__main__":
    key = input()
    A = input().split()
    print(line_search_rec(A, key, 0, len(A) - 1))