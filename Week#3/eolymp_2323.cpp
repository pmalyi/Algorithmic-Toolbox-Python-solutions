// https://eolymp.com/uk/problems/2323
/*
Задано невід’ємне ціле число n. Використовуючи всі його цифри, утворіть найбільше можливе число, а потім — найменше. 
Виведіть суму цих двох чисел.

Наприклад, для n=56002 найбільше число — 65200, а найменше — 256 (початкові нулі в числі 00256 не враховуються). 
Необхідна сума: 65200+256=65456.
*/

#include <iostream>
#include <vector>
#include <algorithm>    
#include <string>

int main() {
    std::string n;
    std::cin >> n;

    // Найменше число
    std::string min_num(n);
    std::sort(min_num.begin(), min_num.end());
    

    // Найбільше число
    std::string max_num(n);
    std::sort(max_num.rbegin(), max_num.rend());

    std::string sum(n.size(), '0'); // Ініціалізуємо рядок для суми нулями

    short carry = 0; // Змінна для переносу при додаванні
    
    // Обчислюємо суму
    for (int i = n.size() - 1; i >= 0; --i) {
        int digit_sum = (max_num[i] - '0') + (min_num[i] - '0') + carry;
        sum[i] = (digit_sum % 10) + '0';
        carry = digit_sum / 10;
    }
    if (carry > 0) {
        sum.insert(sum.begin(), carry + '0'); // Додаємо перенесену цифру на початок
    }
    
    std::cout << sum << std::endl;

    return 0;
}