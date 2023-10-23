def getLastDigitFibonacciSumFast(m, n):
    m = m % 60
    n = n % 60
    if n < m:
        n += 60
    if n < 2:
        return n
    i = 2
    prev = 0
    curr = 1
    sum = 0 if m > 1 else 1
    while i <= n:
        newCurr = curr + prev
        prev = curr
        curr = newCurr
        if i >= m:
            sum += curr
        i += 1
    return sum % 10


m, n = map(int, input().split())
print(getLastDigitFibonacciSumFast(m, n))
