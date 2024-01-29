'''
Виходив з того, що при зростанні поверхів кількість спроб зберігається, поки номер поверху не перевищить
на 1 суму арифметичної прогресії an = 0 + n x 1 для n, що дорівнює кількості спроб.
Звідси і найпростіше інтуїтивно зрозуміле рішення робилося на циклі, що послідовно зчитує суму такої прогресії.
'''

def calcMinThrows(floors):
    suma = 0
    minFloor = 0
    while suma < floors - 1:
        minFloor += 1
        suma += minFloor
    return minFloor


n = int(input())
ans = calcMinThrows(n)
print(ans)

