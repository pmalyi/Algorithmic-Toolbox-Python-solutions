#include <iostream>
#include <vector>
#include <algorithm>

// використаємо алгоритм бінарного пошуку для знаходження позиції вставки елемента в відсортований масив
// це дозволить нам ефективно будувати найтривалішу зростаючу підпослідовність
// time complexity: O(n log n)
// space complexity: O(n)

// функція для бінарного пошуку позиції вставки елемента в відсортований масив
int binary_search(std::vector<int>& arr, int target) {
    int left = 0;
    int right = static_cast<int>(arr.size()) - 1;

    while (left <= right) {
        int mid = (left + right) / 2;

        if (arr[mid] < target) {
            left = mid + 1; // Search in the right half
        } else {
            right = mid - 1; // Search in the left half
        }
    }

    return left; // повертаємо позицію вставки як lower bound (ліва межа)
}


std::vector<int> longest_increasing_subsequence(const std::vector<int>& sequence) {
    std::vector<int> tails; // вектор для зберігання найменшого кінця кожної зростаючої підпослідовності
    std::vector<int> parent(sequence.size(), -1); // вектор для зберігання батьківських елементів
    for (int i = 0; i < static_cast<int>(sequence.size()); ++i) {
        int pos = binary_search(tails, sequence[i]); // знайдемо позицію вставки для поточного числа

        // якщо позиція вставки знаходиться в межах поточного розміру tails, замінюємо елемент на цій позиції
        if (pos < static_cast<int>(tails.size())) { 
            tails[pos] = sequence[i]; // замінюємо елемент на позиції pos
        } else {
            tails.push_back(sequence[i]); // додаємо новий елемент в кінець, якщо він більший за всі елементи в tails
        }
        if (pos > 0){
            parent[i] = tails[pos - 1]; // оновлюємо батьківський індекс для поточного елемента
        }
    }

    std::vector<int> lis; // вектор для зберігання найдовшої зростаючої підпослідовності
    int current_value = tails.back(); // починаємо з останнього елемента в tails
    for (int i = static_cast<int>(sequence.size()) - 1; i >= 0; --i) {
        if (sequence[i] == current_value) { // якщо поточний елемент дорівнює поточному значенню
            lis.push_back(sequence[i]); // додаємо його до результату
            current_value = parent[i]; // оновлюємо поточне значення на батьківський елемент
        }
    }
    std::reverse(lis.begin(), lis.end()); // перевертаємо результат, щоб
    return lis; // повертаємо найтривалішу зростаючу підпослідовність
}  

int main() {
    int test_cases;
    std::cin >> test_cases; // зчитуємо кількість тестових випадків
    std::cin.ignore(); // ігноруємо залишок рядка після зчитування кількості тестових випадків
    std::string line;
    std::getline(std::cin, line); // зчитуємо порожній рядок після кількості тестових випадків
    while (test_cases--) {
        std::vector<int> sequence;

        // Зчитуємо блоки чисел, розділені порожніми рядками
        while (std::getline(std::cin, line)) {
            // Видаляємо можливі символи повернення каретки \r (для Windows-формату файлів)
            if (!line.empty() && line.back() == '\r') {
                line.pop_back();
            }

            if (line.empty()) {
                if (!sequence.empty()) break; // Кінець поточного тесту
                continue;                     // Пропускаємо зайві порожні рядки перед тестом
            }

            sequence.push_back(std::stoi(line));
        }

        if (sequence.empty()) continue;
       
        std::vector<int> lis = longest_increasing_subsequence(sequence); // знаходимо найтривалішу зростаючу підпослідовність

        std::cout << "Max hits: " << lis.size() << std::endl; // виводимо довжину найтривалішої зростаючої підпослідовності
        for (int num : lis) {
            std::cout << num << "\n"; // виводимо елементи найтривалішої зростаючої підпослідовності
        }
        std::cout << std::endl;
    }

    return 0;
}
