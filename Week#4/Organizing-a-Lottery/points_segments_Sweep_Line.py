def count_segments(segments, points):
    """
    Функція рахує, скільки відрізків містять кожну точку.

    segments — список кортежів (l, r)
    points   — список точок
    """

    events = []

    # --- 1. Створюємо події ---
    # Початок відрізка → +1
    # Кінець відрізка   → -1
    for l, r in segments:
        events.append((l, 'L'))  # L = Left (початок)
        events.append((r, 'R'))  # R = Right (кінець)

    # Точки зберігаємо з індексами,
    # щоб після сортування відновити порядок
    for i, p in enumerate(points):
        events.append((p, 'P', i))  # P = Point

    # --- 2. Сортуємо події за координатою, якщо координати одинакові, тоді за типом у порядук: L, P, R---
    events.sort()

    active_segments = 0  # кількість активних відрізків
    result = [0] * len(points)  # відповіді для кожної точки

    # --- 3. Прохід по подіях ---
    for event in events:
        if event[1] == 'L':
            # початок нового відрізка
            active_segments += 1

        elif event[1] == 'R':
            # кінець відрізка
            active_segments -= 1

        else:  # 'P'
            # точка знаходиться всередині active_segments відрізків
            _, _, index = event
            result[index] = active_segments

    return result

n, m = map(int, input().split())
Segments = []
for i in range(n):
    item = tuple(map(int, input().split()))
    Segments.append(item)
Points = tuple(map(int, input().split()[:m]))
resList = count_segments(Segments, Points)
print(*resList)
