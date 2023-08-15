def carFuelingRecurs(current, d, m, gasStations, num_fueling):
    if d <= m:
        return 0
    # current - номер поточної АЗС
    fueling = gasStations[current] # відстань на шляху, де відбулась заправка автомобіля
    while current < len(gasStations) - 1 and gasStations[current + 1] - fueling <= m:
        current += 1
    if gasStations[current] == fueling:
        return "Impossible"
    dist_fueling = gasStations[current] - fueling # дистанція, яку проїхав автомобіль, не заправляючись
    d -= dist_fueling
    num_fueling[0] += 1 # Кількість заправок автомобіля
    return carFuelingRecurs(current, d, m, gasStations, num_fueling)


d = int(input())
m = int(input())
n = int(input())
gasStations = list(map(int, input().split()[:n]))
gasStations.insert(0, 0)
num_fueling = [0,]
result = carFuelingRecurs(0, d, m, gasStations, num_fueling)
if result == "Impossible":
    print(-1)
else:
    print(num_fueling[0])
