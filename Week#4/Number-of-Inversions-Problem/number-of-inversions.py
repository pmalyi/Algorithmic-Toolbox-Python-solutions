def merge(A, B, R):
    n = len(A)
    m = len(B)
    C = []
    j = 0
    i = 0
    count_inversions = 0
    while i < n and j < m:
        if A[i] > B[j]:
            C.append(B[j])
            j += 1
            count_inversions += (n - i)
        else:
            C.append(A[i])
            i += 1
    if i < n:
        C.extend(A[i:])
    else:
        C.extend(B[j:])
    R.append(count_inversions)
    return C


def mergeSortRec(myList):
    if len(myList) < 2:
        return myList[:]
    else:
        middle = len(myList) // 2
        left = mergeSortRec(myList[:middle])
        right = mergeSortRec(myList[middle:])
        return merge(left, right, resList)


n = int(input())
myList = list(map(int, input().split()[:n]))
resList = []
newList = mergeSortRec(myList)
#print(newList)
#print(resList)
print(sum(resList))
