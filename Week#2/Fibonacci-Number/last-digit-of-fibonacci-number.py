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


n = int(input())
n %= 60
print(phib(n) % 10)
