def isBetter(s1, s2):
    res1 = int(s1 + s2)
    res2 = int(s2 + s1)
    if res1 >= res2:
        return True
    return False


def largestConcatenate(Numbers):
    yourSalaryList = []
    while len(Numbers) > 0:
        best_number = Numbers[0]
        best_index = 0
        for i in range(1, len(Numbers)):
            if isBetter(Numbers[i], best_number):
                best_number = Numbers[i]
                best_index = i
        yourSalaryList.append(best_number)
        Numbers.pop(best_index)
    yourSalary = ''.join(yourSalaryList)
    return yourSalary


n = int(input())
strList = list(map(str, input().split()))
print(largestConcatenate(strList))
