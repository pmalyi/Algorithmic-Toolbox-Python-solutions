from merge import merge_arr

def merge_sort(a, left, right):
    if left >= right:
        return

    middle = (left + right) // 2

    merge_sort(a, left, middle)
    merge_sort(a, middle + 1, right)
    merge_arr(a, left, middle, right)


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)

