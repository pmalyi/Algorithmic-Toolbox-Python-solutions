from merge import merge

def merge_sort(arr):
    """
    Функція сортує список arr за допомогою алгоритму Merge Sort
    та повертає новий відсортований список
    """

    # Базовий випадок рекурсії:
    # список з 0 або 1 елемента вже відсортований
    if len(arr) <= 1:
        return arr

    # 1. Ділимо список навпіл
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 2. Рекурсивно сортуємо обидві половини
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # 3. Зливаємо дві відсортовані половини
    return merge(left_sorted, right_sorted)


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    result = merge_sort(arr)
    print(result)