'''
https://eolymp.com/uk/problems/11244
Дано масив A з n цілих чисел, відсортований за зростанням. Визначте, чи існує в ньому така пара чисел (A[i], A[j]) де i<j, 
сума яких дорівнює x.
'''

n, x = map(int, input().split())
A = tuple(map(int, input().split()))

# Використовуємо два вказівники для пошуку пари чисел, сума яких дорівнює x
left, right = 0, n - 1
found = False   
while left < right:
    current_sum = A[left] + A[right]
    if current_sum == x:
        found = True
        break
    elif current_sum < x:
        left += 1  # Збільшуємо лівий вказівник, щоб збільшити суму
    else:
        right -= 1  # Зменшуємо правий вказівник, щоб зменшити суму

if found:
    print("YES")
else:
    print("NO")
    