# Зчитуємо розміри таблиці
n, m = map(int, input().split())

# Зчитуємо таблицю з кислотою
acid = []
for _ in range(n):
    acid.append(list(map(int, input().split())))

# Замість створення нової таблиці, ми просто перезаписуємо вхідну
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0: # перший рядок
            acid[i][j] += acid[i][j-1]
        elif j == 0: # перший стовпчик
            acid[i][j] += acid[i-1][j]
        else:
            acid[i][j] += min(acid[i-1][j], acid[i][j-1])
print(acid[n-1][m-1])