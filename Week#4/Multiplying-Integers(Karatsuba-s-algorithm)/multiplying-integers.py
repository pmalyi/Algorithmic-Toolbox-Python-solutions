from math import ceil
def karatsuba(X, Y):
    n = max(len(X), len(Y))
    if n <= 1:
        return int(X) * int(Y)
    mid_pow = ceil(n / 2)
    mid_split = n // 2
    if len(X) == n:
        A = X[:mid_split]
        B = X[mid_split:]
        Y = (len(X) - len(Y)) * '0' + Y
        C = Y[:mid_split]
        D = Y[mid_split:]
    else:
        X = (len(Y) - len(X)) * '0' + X
        A = X[:mid_split]
        B = X[mid_split:]
        C = Y[:mid_split]
        D = Y[mid_split:]
    P = karatsuba(A, C) # A * C
    Q = karatsuba(str(int(A) + int(B)), str(int(C) + int(D)))  # (A + B) * (C + D)
    R = karatsuba(B, D) # B * D

    return 10 ** (mid_pow * 2) * P + 10 ** mid_pow * (Q - P - R) + R


def stressTest():
    for num1 in range(1000):
        flag = False
        for num2 in range(1000):
            res1 = karatsuba(str(num1), str(num2))
            res2 = num1 * num2
            if res1 != res2:
                print('Faild')
                print('Karatsuba:', num1, '*', num2, '=', res1)
                print('Simple:', num1, '*', num2, '=', res2)
                flag = True
        if flag:
            break
    else:
        print('The stres-test was successful')


stressTest()
# num1, num2 = map(str, input().split())
# print(karatsuba(num1, num2))
# print(int(num1) * int(num2))
