def carFueling(d, m, gasStations):
    n = len(gasStations)
    current = 0 # current - номер поточної АЗС
    fueling = gasStations[current] # відстань на шляху, де відбулась заправка автомобіля
    num_fueling = 0 # Кількість заправок автомобіля
    while d > m:
        while current < n - 1 and gasStations[current + 1] - fueling <= m:
            current += 1
        if gasStations[current] == fueling:
            return -1
        print(gasStations[current])
        dist_fueling = gasStations[current] - fueling # дистанція, яку проїхав автомобіль, не заправляючись
        d -= dist_fueling
        num_fueling += 1
    return num_fueling


d = int(input())
m = int(input())
n = int(input())
gasStations = list(map(int, input().split()[:n]))
gasStations.insert(0, 0)
print(carFueling(d, m, gasStations))