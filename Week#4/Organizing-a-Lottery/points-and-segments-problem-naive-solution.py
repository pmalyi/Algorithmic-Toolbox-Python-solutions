# time limit exceeded
def pointsAndSegments(Segments, Points):
    resList = [0] * len(Points)
    Segments.sort(key=lambda X: X[1])
    numPoints = []
    for i in range(len(Points)):
        item = (Points[i], i)
        numPoints.append(item)
    numPoints.sort()
    start_segment_index = 0
    for point in numPoints:
        count_contained = 0
        segment_index = start_segment_index
        while segment_index < len(Segments):
            if point[0] > Segments[segment_index][1]:
                start_segment_index += 1
                segment_index = start_segment_index
            elif point[0] >= Segments[segment_index][0]:
                count_contained += 1
                segment_index += 1
            else:
                break
        resList[point[1]] = count_contained
    return resList


n, m = map(int, input().split())
Segments = []
for i in range(n):
    item = tuple(map(int, input().split()))
    Segments.append(item)
Points = list(map(int, input().split()[:m]))
resList = pointsAndSegments(Segments, Points)
print(*resList)
