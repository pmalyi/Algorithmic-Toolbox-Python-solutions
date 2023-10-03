def lis(A):
    n = len(A)
    # Будуємо динамічний масив T
    T = [1] * n
    # Будуємо масив з номерів елементів, які були останніми, що призвели до збільшення елемента масиву Т
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and T[i] < T[j] + 1:
                T[i] += 1
                prev[i] = j
    # Знаходимо номер першого максимального елемента масиву Т
    last = 0
    for i in range(1, n):
        if T[i] > T[last]:
            last = i
    # Використовуючи масив prev здійснюємо трасування (відтворення найдовшої зростаючої підпослідовності)
    current = last
    # Будуємо масив номерів послідовності, рухаючись з кінця
    tracing = []
    while current > 0:
        tracing.append(current)
        current = prev[current]
    tracing.reverse()
    # Найдовша зростаюча підпослідовність (зазвичай, одна з декількох)
    LIS = [A[i] for i in tracing]
    return T, prev, tracing, LIS, max(T)


A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
DP, prev, tracing, LIS, len_lis = lis(A)
print('Input array:', A)
print('Dynamic array:', DP)
print('Previous array:', prev)
print('Tracing index array:', tracing)
print('Longest increasing subsequence:', LIS)
print('Length longest increasing subsequence:', len_lis)