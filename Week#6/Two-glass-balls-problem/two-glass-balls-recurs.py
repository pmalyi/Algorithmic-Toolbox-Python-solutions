def calcMinThrows(floors):
    if floors < 3:
        return floors - 1

    minFloor = floors - 1
    for currentFloor in range(1, floors):
        worstFloorIfBroken = currentFloor - 1
        worstFloorIfSaved = calcMinThrows(floors - currentFloor)
        optimalFloor = max(worstFloorIfBroken, worstFloorIfSaved)
        minFloor = min(minFloor, optimalFloor)
    return minFloor + 1

# or
    '''
    minFloor = floors - 1
    for currentFloor in range(1, floors):
        minFloor = min(minFloor, max(currentFloor, calcMinThrows(floors - currentFloor) + 1))
    return minFloor
    '''

n = int(input())
ans = calcMinThrows(n)
print(ans)

