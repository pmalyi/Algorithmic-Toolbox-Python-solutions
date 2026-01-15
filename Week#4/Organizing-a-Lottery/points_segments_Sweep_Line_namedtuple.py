from collections import namedtuple

# Опис події за допомогою іменованого кортежу
# x     — координата на прямій
# kind  — тип події ('L' — початок, 'R' — кінець, 'P' — точка)
# index — індекс точки (потрібен лише для 'P')
Event = namedtuple('Event', ['x', 'kind', 'index'])


def count_segments(segments, points):
    """
    Рахує, скільки відрізків містять кожну точку.

    segments — список відрізків (l, r)
    points   — список точок
    """

    events = []

    # --- 1. Створення подій для відрізків ---
    for l, r in segments:
        events.append(Event(l, 'L', None))       # початок відрізка
        events.append(Event(r, 'R', None))   # кінець відрізка

    # --- 2. Створення подій для точок ---
    for i, p in enumerate(points):
        events.append(Event(p, 'P', i))          # точка з індексом

    # --- 3. Сортування всіх подій за координатою, якщо координати одинакові, тоді за типом у порядук: L, P, R ---
    events.sort(key=lambda e: (e.x, e.kind))

    active_segments = 0                  # кількість активних відрізків
    result = [0] * len(points)           # відповіді для точок

    # --- 4. Прохід по подіях ---
    for event in events:
        if event.kind == 'L':
            # починається новий відрізок
            active_segments += 1

        elif event.kind == 'R':
            # завершується відрізок
            active_segments -= 1

        else:  # event.kind == 'P'
            # у цій точці активні всі поточні відрізки
            result[event.index] = active_segments

    return result


n, m = map(int, input().split())
Segments = []
for i in range(n):
    item = tuple(map(int, input().split()))
    Segments.append(item)
Points = tuple(map(int, input().split()[:m]))
resList = count_segments(Segments, Points)
print(*resList)