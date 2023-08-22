def isBetter(s1, s2):
    res1 = int(s1 + s2)
    res2 = int(s2 + s1)
    if res1 >= res2:
        return True
    return False


def largestConcatenate(Numbers, resultList):
    if len(Numbers) > 0:
        best_number = Numbers[0]
        best_index = 0
        for i in range(1, len(Numbers)):
            if isBetter(Numbers[i], best_number):
                best_number = Numbers[i]
                best_index = i
        resultList.append(best_number)
        Numbers.pop(best_index)
        largestConcatenate(Numbers, resultList)


n = int(input())
strList = list(map(str, input().split()))
yourSalaryList = []
largestConcatenate(strList, yourSalaryList)
print(''.join(yourSalaryList))
