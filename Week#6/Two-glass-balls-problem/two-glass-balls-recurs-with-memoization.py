memoization = {}

def calcMinThrows(floors):
    if floors <= 3:
        return floors - 1
    if floors not in memoization: # залучення мемоїзації
        minFloor = floors - 1
        for currentFloor in range(floors - 1, 0, -1): #цикл по номерах поверхів свідомо іде зверху вниз, щоб рекурсиві
        # виклики 	calcMinThrows(floors - currentFloor) починались с малих значень кількості поверхів, це
        # дозволить оптимально задіяти мемоїзацію!
            minFloor = min(minFloor, max(currentFloor, calcMinThrows(floors - currentFloor) + 1))
            # вибираємо варіант з найбільшою кількістю кидків з двох можливих сценаріїв развитку подій
            # (перша кулька розбилась/не разбилась)
            memoization[floors] = minFloor
    return memoization[floors]


n = int(input())
ans = calcMinThrows(n)
print(ans)
