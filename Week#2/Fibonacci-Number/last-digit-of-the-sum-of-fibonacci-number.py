def getLastDigitFibonacciSumFast(m, n):
    m = m % 60
    n = n % 60
    if n < 2:
        return n
    i = 2
    prev = m
    curr = 1
    sum = prev + curr
    while i <= n:
        newCurr = curr + prev
        prev = curr
        curr = newCurr
        sum += curr
        i += 1
    return sum % 10


n = int(input())
print(getLastDigitFibonacciSumFast(0, n))
