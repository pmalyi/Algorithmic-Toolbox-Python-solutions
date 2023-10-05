T = dict()


def edit_distance(a, b, i, j):
    if not (i, j) in T:
        if i == 0:
            T[i, j] = j
        elif j == 0:
            T[i, j] = i
        else:
            diff = 0 if a[i - 1] == b[j - 1] else 1
            T[i, j] = min(edit_distance(a, b, i - 1, j) + 1,
                          edit_distance(a, b, i, j - 1) + 1,
                          edit_distance(a, b, i - 1, j - 1) + diff)
    return T[i, j]


print(edit_distance(a="editing", b="distance", i=7, j=8))
print(T)
for j in range(9):
    for i in range(8):
        print(T[i, j], end=' ')
    print()
