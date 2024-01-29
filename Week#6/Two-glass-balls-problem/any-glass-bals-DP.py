# Завдання про скляні кулі – рішення в загальному випадку
def calcMinThrows(floors, balls):
    dp = [[0] * balls for _ in range(floors + 1)]
    for i in range(floors + 1):
        dp[i][0] = i - 1
    for ball in range(1, balls):
        dp[1][ball] = 0
        dp[2][ball] = 1
        for maxFloor in range(3, floors + 1):
            minFloor = floors
            for currentFloor in range(1, maxFloor + 1):
                worstFloorIfBroken = dp[currentFloor][ball - 1]
                worstFloorIfSaved = dp[maxFloor - currentFloor][ball]
                optimalFloor = max(worstFloorIfBroken, worstFloorIfSaved)
                if optimalFloor < minFloor:
                    minFloor = optimalFloor
            dp[maxFloor][ball] = minFloor + 1
    return dp[floors][balls - 1], dp


n, k = map(int, input().split())
ans, ansArr = calcMinThrows(n, k)
outF = open('output.txt', 'w')
print(ans, file=outF)
print("fl/b", end="", file=outF)
for ball in range(1, k + 1):
    print(str(ball).rjust(3), end='|', file=outF)
print('\n'+('-'*k*4 + '-'*4), file=outF)
for ind_floor in range(1, len(ansArr)):
    print(f'{str(ind_floor).rjust(3)}:', end='', file=outF)
    for p in ansArr[ind_floor]:
        print(str(p).rjust(3), end='|', file=outF)
    print('\n'+('-'*len(ansArr[ind_floor]*4) + '-'*4), file=outF)
outF.close()
