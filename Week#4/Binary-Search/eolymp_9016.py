'''
https://eolymp.com/uk/problems/9016
'''
def is_number_in_array(arr, k):
    low, high = 0, len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == k:
            return True
        elif arr[middle] < k:
            low = middle + 1
        else:
            high = middle - 1
    return False


if __name__ == '__main__':
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(q):
        k = int(input())
        print('YES' if is_number_in_array(arr, k) else 'NO')
        
