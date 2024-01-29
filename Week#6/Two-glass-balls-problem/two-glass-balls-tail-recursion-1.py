def calcMinThrows(floors, ball):
    if floors <= 1:
        return ball

    ball += 1
    return calcMinThrows(floors - ball, ball)

n = int(input())
if n == 1:
    print(0)
else:
    ans = calcMinThrows(n - 1, 1)
    print(ans)
