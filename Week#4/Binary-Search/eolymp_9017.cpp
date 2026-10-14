/*
https://eolymp.com/uk/problems/9017

Задано відсортований масив із n цілих чисел. Вам слід відповісти на q запитів: скільки разів задане число x 
міститься в масиві.

Вхідні дані
У першому рядку містяться два числа n і q (n,q<=10^6). Другий рядок містить n цілих чисел, відсортованих за зростанням. 
Кожен із наступних q рядків містить одне значення x. Усі числа в масиві за модулем не перевищують 10^9.

Вихідні дані
Для кожного значення x виведіть в окремому рядку кількість його входжень у масив.

Приклади
Вхідні дані #1
6 3
2 4 4 8 11 14
10
4
2
Відповідь #1
0
2
1
*/

#include <iostream>
#include <vector>   
#include <algorithm>

/*
size_t lower_bound(const std::vector<int>& arr, size_t n, int x) {
    size_t left = 0, right = n;
    while (left < right) {
        size_t mid = (left + right) / 2;
        if (arr[mid] < x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left; // Повертає індекс першого елемента, який не менший за x
}

size_t upper_bound(const std::vector<int>& arr, size_t n, int x) {
    size_t left = 0, right = n;
    while (left < right) {
        size_t mid = (left + right) / 2;
        if (arr[mid] <= x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left; // Повертає індекс першого елемента, який більший за x
}
*/

int lower_bound(const std::vector<int>& arr, size_t n, int x) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left; // Повертає індекс першого елемента, який не менший за x
}

int upper_bound(const std::vector<int>& arr, int n, int x) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] <= x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return right; 
}

int main() {
    int n, q;
    std::cin >> n >> q;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    for (int i = 0; i < q; ++i) {
        int x;
        std::cin >> x;

        int lower = lower_bound(arr, n, x); // Індекс першого входження x
        int upper = upper_bound(arr, n, x); // Індекс першого елемента, який більший за x
        // size_t count = upper - lower; // Кількість входжень x у масиві
        int count = upper - lower + 1; // Кількість входжень x у масиві

        std::cout << count << std::endl;
    }

    return 0;
}