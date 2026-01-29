# https://academy.yandex.ru/handbook/algorithms/article/zadacha-para-blizhajshih-tochek
# Реалізація алгоритму "найближча пара точок" методом розділяй і володарюй

from math import sqrt  # Імпортуємо функцію sqrt для обчислення квадратного кореня


# Функція для обчислення квадрату відстані між двома точками
def distance(p1, p2):
    # Повертаємо квадрат евклідової відстані: (x1 - x2)^2 + (y1 - y2)^2
    # Використовуємо квадрат відстані, щоб уникнути непотрібного виклику sqrt на кожному кроці
    return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])


# Рекурсивна функція для пошуку мінімальної відстані між точками у відрізку Points[low..high]
def getMinDistance(Points, low, high):
    # Якщо залишилось лише дві точки, просто повертаємо відстань між ними
    if high - low == 1:
        return distance(Points[low], Points[high])

    # Якщо три точки, перевіряємо всі три можливі пари і беремо мінімум
    if high - low == 2:
        d1 = distance(Points[low], Points[low + 1])
        d2 = distance(Points[low + 1], Points[high])
        d3 = distance(Points[low], Points[high])
        return min(d1, d2, d3)

    # Інакше, ділимо множину точок на дві половини
    mid = low + (high - low) // 2

    # Рекурсивно знаходимо мінімальні відстані у лівій і правій половинах
    dist1 = getMinDistance(Points, low, mid)
    dist2 = getMinDistance(Points, mid + 1, high)

    # Мінімальна відстань серед лівої та правої половин
    dist = min(dist1, dist2)

    # Визначаємо середню точку для смуги Strip
    if (high - low) % 2 != 0:
        rmid = mid + 1
    else:
        rmid = mid
    left = mid
    right = rmid

    # Формуємо смугу Strip шириною sqrt(dist) по x, де може бути мінімальна пара
    while left >= low:
        # Відкидаємо точки, що знаходяться далі sqrt(dist) від середньої точки зліва
        if Points[mid][0] - Points[left][0] - sqrt(dist) < 0.001:
            left -= 1
        else:
            break
    if left < low:
        left = low

    while right <= high:
        # Відкидаємо точки, що знаходяться далі sqrt(dist) від середньої точки справа
        if Points[right][0] - Points[rmid][0] - sqrt(dist) < 0.001:
            right += 1
        else:
            break
    if right > high:
        right = high

    # Створюємо список точок, що потрапляють у смугу Strip
    Strip = Points[left:right + 1]

    # Сортуємо точки смуги по y-координаті
    Strip.sort(key=lambda X: X[1])

    # Перевіряємо всі пари точок у смузі, але не більше ніж 7 наступних точок
    for p in range(len(Strip) - 1):
        q = p + 1
        step = 0
        while q < len(Strip) and step < 7:
            # Обчислюємо відстань між точками Strip[p] і Strip[q]
            cur_dist = distance(Strip[p], Strip[q])
            # Оновлюємо мінімальну відстань
            dist = min(dist, cur_dist)
            q += 1
            step += 1

    # Повертаємо мінімальну відстань (квадрат)
    return dist


# -------------------
# Основна частина програми
# -------------------

n = int(input())  # Зчитуємо кількість точок

# Зчитуємо точки у вигляді списку кортежів (x, y)
points = [tuple(map(int, input().split())) for i in range(n)]

'''
# Альтернативно, зчитування з файлу
with open('input1.txt', 'r', encoding='utf-8') as inF:
    n = int(inF.readline())
    points = [tuple(map(int, inF.readline().split())) for i in range(n)]
'''

# Сортуємо точки по x-координаті перед застосуванням алгоритму "розділяй і володарюй"
points.sort()

# Викликаємо рекурсивну функцію і беремо квадратний корінь, щоб отримати справжню відстань
res = sqrt(getMinDistance(points, 0, n - 1))

# Виводимо результат
print(res)
