# не проходить всі тести
def isBetter(s1, s2):
    if s1 == s2:
        return True
    i = 0
    j = 0
    l1 = len(s1)
    l2 = len(s2)
    while s1[i] == s2[j]:
        if l1 > i + 1:
            i += 1
        if l2 > j + 1:
            j += 1
        if max(i, j) == max(l1 - 1, l2 - 1):
            while s1[i] == s2[j]:
                i -= 1
                j -= 1
    if s1[i] > s2[j]:
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
