def merge_arr(a, left, middle, right):
    # Тимчасовий масив для злиття
    tmp = [0] * (right - left + 1)

    i = left          # індекс лівої частини
    j = middle + 1    # індекс правої частини
    k = 0             # індекс tmp

    # Злиття двох відсортованих підмасивів
    while i <= middle and j <= right:
        if a[i] < a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1

    # Копіюємо залишки з лівої частини
    while i <= middle:
        tmp[k] = a[i]
        i += 1
        k += 1

    # Копіюємо залишки з правої частини
    while j <= right:
        tmp[k] = a[j]
        j += 1
        k += 1

    # Переносимо результат назад у масив a
    for t in range(left, right + 1):
        a[t] = tmp[t - left]
