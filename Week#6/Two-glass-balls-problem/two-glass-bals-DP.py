def calcMinThrows(floors, balls):
    if balls == 1 or floors <= 2:
        return floors - 1
    dp = [[0] * balls for _ in range(floors + 1)]
    for i in range(floors + 1):
        dp[i][0] = i
    for ball in range(1, balls):
        dp[1][ball] = 0
        dp[2][ball] = 1
        for maxFloor in range(3, floors + 1):
            minFloor = floors
            for currentFloor in range(1, maxFloor + 1):
                worstFloorIfBroken = dp[currentFloor - 1][ball - 1]
                worstFloorIfSaved = dp[maxFloor - currentFloor][ball]
                optimalFloor = max(worstFloorIfBroken, worstFloorIfSaved)
                if optimalFloor < minFloor:
                    minFloor = optimalFloor
            dp[maxFloor][ball] = minFloor + 1
    return dp[floors][balls - 1], dp


n, k = map(int, input().split())
ans, ansArr = calcMinThrows(n, k)
print(ans)
for row in ansArr:
    print(*row)
