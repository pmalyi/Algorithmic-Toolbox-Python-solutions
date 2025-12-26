def merge(left, right):
    """
    Зливає два відсортовані списки left і right
    в один відсортований список
    """

    result = []   # Результуючий список
    i = j = 0     # Індекси для left і right

    # Поки в обох списках є елементи
    while i < len(left) and j < len(right):

        # Беремо менший елемент
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):  # Якщо залишилися елементи в left
        result.extend(left[i:])
    else:   # Якщо залишилися елементи в right
        result.extend(right[j:])

    return result
