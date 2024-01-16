def calcMinThrows(floors, balls):
    if balls == 1 or floors <= 2:
        return floors - 1
    minFloor = floors
    for currentFloor in range(3, floors + 1):
        worstFloorIfBroken = calcMinThrows(currentFloor - 1, balls - 1)
        worstFloorIfSaved = calcMinThrows(floors - currentFloor, balls)
        optimalFloor = max(worstFloorIfBroken, worstFloorIfSaved)
        if optimalFloor < minFloor:
            minFloor = optimalFloor

    return minFloor + 1


n, k = map(int, input().split())
ans = calcMinThrows(n, k)
print(ans)
