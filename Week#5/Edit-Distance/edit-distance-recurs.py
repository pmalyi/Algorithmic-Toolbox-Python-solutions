def edit_distance(a, b, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    diff = 0 if a[i - 1] == b[j - 1] else 1
    result = min(edit_distance(a, b, i - 1, j) + 1,
                 edit_distance(a, b, i, j - 1) + 1,
                 edit_distance(a, b, i - 1, j - 1) + diff)
    return result


print(edit_distance(a="editing", b="distance", i=7, j=8))

