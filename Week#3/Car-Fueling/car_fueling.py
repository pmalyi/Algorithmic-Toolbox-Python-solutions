def carFueling(d, m, gasStations):
    n = len(gasStations)
    current = 0 # current - номер поточної АЗС
    fuelinf = gasStations[current] # відстань на шляху, де відбулась заправка автомобіля
    num_fueling = 0 # Кількість заправок автомобіля
    while d > m:
        while current < n - 1 and gasStations[current + 1] - fuelinf <= m:
            current += 1
        if gasStations[current] == fuelinf:
            return -1
        dist_fueling = gasStations[current] - fuelinf # дистанція, яку проїхав автомобіль, не заправляючись
        d -= dist_fueling
        num_fueling += 1
    return num_fueling


d = int(input())
m = int(input())
n = int(input())
gasStations = list(map(int, input().split()[:n]))
gasStations.insert(0, 0)
print(carFueling(d, m, gasStations))
