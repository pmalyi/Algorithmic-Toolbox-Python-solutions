# https://cses.fi/problemset/task/1073
def find_first_greater(towers, x):
    """
    Шукає індекс першого елемента в towers, який > x.
    """
    low = 0
    high = len(towers) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if towers[mid] > x:
            # Якщо елемент більший, він може бути нашою відповіддю,
            # але ми шукаємо найменший серед таких, тому йдемо вліво.
            ans = mid
            high = mid - 1
        else:
            # Якщо елемент <= x, нам потрібно шукати тільки правіше.
            low = mid + 1
    return ans


def solve(cubes):

    # Список верхівок веж (завжди буде відсортованим)
    towers = []

    for x in cubes:
        # Шукаємо індекс вежі за допомогою нашої функції
        idx = find_first_greater(towers, x)

        if idx != -1:
            # Якщо знайшли вежу з верхівкою > x, оновлюємо її
            towers[idx] = x
        else:
            # Якщо всі верхівки <= x, додаємо нову вежу
            towers.append(x)

    return len(towers)


if __name__ == "__main__":
    n = int(input())
    cubes = map(int, input().split())
    print(solve(cubes))