def gasStationSearch(curr, fueling, n, gasStations): # пошук оптимальної АЗС
    while curr < n - 1 and gasStations[curr + 1] - fueling <= m:
        curr += 1
    return curr # повертаємо номер АЗС, на якій потрібно робити заправку автомобіля


def carFueling(d, m, gasStations):
    n = len(gasStations)
    current = 0 # current - номер поточної АЗС
    fueling = gasStations[current] # відстань на шляху, де відбулась заправка автомобіля
    num_fueling = 0 # Кількість заправок автомобіля
    while d > m:
        current = gasStationSearch(current, fueling, n, gasStations)  # оптимальний "жадібний" вибір
        if gasStations[current] == fueling: # не вдалося знайти АЗС відстань до якої не перевищує m
            return -1
        dist_fueling = gasStations[current] - fueling # дистанція, яку проїхав автомобіль, не заправляючись
        d -= dist_fueling # зменшуємо загальну відстань (обсяг задачі)
        fueling = gasStations[current]  # перевизначаємо відстань на шляху, де відбулась заправка автомобіля
        num_fueling += 1  # інкрементуємо кількість заправок автомобіля
    return num_fueling


d = int(input()) # загальна відстань, яку повинен проїхати автомобіль (обсях задачі)
m = int(input())  # відстань, яку може проїхати автомобіль на повному баку
n = int(input())  # кількість АЗС на шляху між містами
gasStations = list(map(int, input().split()[:n]))  # масив, що містить відстані від початку дистанції до кожної АЗС
gasStations.insert(0, 0)  # додаємо до масиву у нкльову позицію значення 0, оскільки за умовою
                                            # автомобіль стартує з повним баком
print(carFueling(d, m, gasStations))
