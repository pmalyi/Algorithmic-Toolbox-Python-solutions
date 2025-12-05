def line_search(A, key, low, high):
    for i in range(low, high + 1):
        if A[i] == key:
            return i
    return "not found"


if __name__ == "__main__":
    key = input()
    A = input().split()
    #print(A.index(key))
    print(line_search(A, key, 0, len(A) - 1))