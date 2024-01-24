def calcMinThrows(floors):
    if floors <= 3:
        return floors - 1
    minFloor = floors
    for currentFloor in range(1, floors + 1):
        worstFloorIfBroken = currentFloor - 1
        worstFloorIfSaved = calcMinThrows(floors - currentFloor)
        optimalFloor = max(worstFloorIfBroken, worstFloorIfSaved)
        if optimalFloor < minFloor:
            minFloor = optimalFloor

    return minFloor + 1


n = int(input())
ans = calcMinThrows(n)
print(ans)
