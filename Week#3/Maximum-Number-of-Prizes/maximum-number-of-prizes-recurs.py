def distinctSummands(nList, i, resultList):
    if nList[0] < i:
        return 0
    resultList.append(i)
    nList[0] -= i
    i += 1
    return 1 + distinctSummands(nList, i, resultList)


num = int(input())
myList = []
nList = [num,]
count = distinctSummands(nList, 1, myList)
myList[-1] += nList[0]
print(count)
print(*myList)