# Compute the n-th Fibonacci number modulo m.
def pisanoPeriod(m):
    if m <= 1:
        return m
    f0 = 0
    f1 = 1
    i = 2
    while i <= 6 * m:
        fi = (f0 + f1) % m
        f0 = f1
        f1 = fi
        if f0 == 0 and f1 == 1:
            return i - 1
        i += 1

def phib(n):
    if n <= 1:
        return n
    f0 = 0
    f1 = 1
    fi = 0
    i = 2
    while i <= n:
        fi = f0 + f1
        f0 = f1
        f1 = fi
        i += 1
    return fi


n, m = map(int, input().split())
p = pisanoPeriod(m)
n = n % p
phib = phib(n)
res = phib % m
print(res)
