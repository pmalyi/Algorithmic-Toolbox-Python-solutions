import sys
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def longest_increasing_subsequence(arr):
    n = len(arr)
    tails = [] # зберігає найменший кінець для всіх зростаючих підпослідовностей з різною довжиною
    
    for i in range(n):
        pos = binary_search(tails, arr[i]) # знайти позицію для вставки arr[i] в tails
        
        if pos < len(tails): # якщо позиція знаходиться в межах поточного розміру tails, замінити елемент на цій позиції
            tails[pos] = arr[i] 
        else: # інакше додати arr[i] в кінець tails
            tails.append(arr[i])
        
    return len(tails), tails # повертаємо довжину та саму послідовність

test_cases = int(input().strip())
input() # пропускаємо порожній рядок
for _ in range(test_cases):
    heights = []
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        heights.append(int(line))
        
    max_hits, sequence = longest_increasing_subsequence(heights)
    print(f"Max hits: {max_hits}")
    for height in sequence:
        print(height)
    print() # порожній рядок між тестами