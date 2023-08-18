def coveringSegmentsByPoints(left, right, resultPoints):
    if len(right) == 0:
        return 0
    right_min = min(right)
    resultPoints.append(right_min)
    i = 0
    while i < len(right):
        if left[i] <= right_min:
            left.pop(i)
            right.pop(i)
        else:
            i += 1
    return 1 + coveringSegmentsByPoints(left, right, resultPoints)


n = int(input())
left = []
right = []
resultPoints = []
for i in range(n):
    l, r = map(int, input().split())
    left.append(l)
    right.append(r)
print(coveringSegmentsByPoints(left, right, resultPoints))
print(*resultPoints)