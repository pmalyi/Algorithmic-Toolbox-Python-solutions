def primCalc(n):
    if n == 1:
        return 0
    div3 = n
    div2 = n
    minus1 = primCalc(n - 1)
    if (n // 3 >= 1) and (n % 3 == 0):
        div3 = primCalc(n // 3)
    if (n // 2 >= 1) and (n % 2 == 0):
        div2 = primCalc(n // 2)
    return 1 + min(div3, div2, minus1)


n = int(input())
print(primCalc(n))