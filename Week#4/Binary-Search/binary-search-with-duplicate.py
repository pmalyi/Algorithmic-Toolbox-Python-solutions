def first_occurrence(a, x, left, right):
    """Пошук першого входження x у відсортованому масиві a."""
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            result = mid
            right = mid - 1   # шукаємо перше входження
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result


# --- зчитування введення ---
n = int(input())
k = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

left, right = 0, n - 1
# --- обробка запитів ---
for x in q:
    print(first_occurrence(k, x, left, right), end=' ')

