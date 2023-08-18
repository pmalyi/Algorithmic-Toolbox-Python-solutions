def coveringSegmentsByPoints(myList):
    resultPoints = []
    myList.sort(key=lambda A: A[1])
    while len(myList) != 0:
        point = myList[0][1]
        # point = min(map(lambda X: X[1], myList))
        resultPoints.append(point)
        i = 0
        while i < len(myList):
            if myList[i][0] <= point:
                myList.pop(i)
            else:
                i += 1
    return resultPoints


n = int(input())
inList =[]
for i in range(n):
    item = tuple(map(int, input().split()))
    inList.append(item)
outList = coveringSegmentsByPoints(inList)
print(len(outList))
print(*outList)
