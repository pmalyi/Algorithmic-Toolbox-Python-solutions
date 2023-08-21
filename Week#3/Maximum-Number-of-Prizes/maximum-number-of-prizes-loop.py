def distinctSummands(n):
    resultList = []
    i = 1
    while i <= n:
        resultList.append(i)
        n -= i
        i += 1
    resultList[-1] += n
    return resultList


n = int(input())
myList = distinctSummands(n)
print(len(myList))
print(*myList)
