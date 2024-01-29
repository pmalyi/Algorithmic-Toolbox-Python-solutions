def calcMinThrows(floors, ball, suma):
    if suma + ball >= floors - 1:
        return ball
    return calcMinThrows(floors, ball + 1, suma + ball)

n = int(input())
if n == 1:
    print(0)
else:
    ans = calcMinThrows(n, 1, 0)
    print(ans)