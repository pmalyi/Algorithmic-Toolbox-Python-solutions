def pointsAndSegments(Lefts, Rights, Points, m):
    left_label, point_label, right_label = 0, 1, 2
    resList = [0] * m
    combined = []
    for l in Lefts:
        combined.append((l, left_label))
    for r in Rights:
        combined.append((r, right_label))
    for i, p in enumerate(Points):
        combined.append((p, point_label, i))
    combined.sort()
    count_contained = 0
    for item in combined:
        if item[1] == left_label:
            count_contained += 1
        elif item[1] == right_label:
            count_contained -= 1
        else:
            resList[item[2]] = count_contained
    return resList


n, m = map(int, input().split())
Lefts = []
Rights =[]
for i in range(n):
    l, r = map(int, input().split())
    Lefts.append(l)
    Rights.append(r)
Points = list(map(int, input().split()[:m]))
resList = pointsAndSegments(Lefts, Rights, Points, m)
print(*resList)
