from math import ceil
def karatsuba(X, Y):
    if len(X) == 1 or len(Y) == 1:
        return int(X) * int(Y)
    n = max(len(X), len(Y))
    # mid_pow = ceil(n / 2)
    middle = n // 2
    A = X[:-middle]
    B = X[-middle:]
    C = Y[:-middle]
    D = Y[-middle:]
    P = karatsuba(A, C) # A * C
    Q = karatsuba(str(int(A) + int(B)), str(int(C) + int(D)))  # (A + B) * (C + D)
    R = karatsuba(B, D) # B * D
    return 10 ** (middle * 2) * P + 10 ** middle * (Q - P - R) + R


def stressTest():
    for num1 in range(1000):
        flag = False
        for num2 in range(1000):
            res1 = karatsuba(str(num1), str(num2))
            res2 = num1 * num2
            if res1 != res2:
                print('Fail')
                print('Karatsuba:', num1, '*', num2, '=', res1)
                print('Simple:', num1, '*', num2, '=', res2)
                flag = True
        if flag:
            break
    else:
        print('The stress-test was successful')


stressTest()
# num1, num2 = map(str, input().split())
# print(karatsuba(num1, num2))
# print(int(num1) * int(num2))
