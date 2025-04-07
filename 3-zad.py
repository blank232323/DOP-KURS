#include <iostream>
#include <vector>

std::vector<int> filter_greater_than(const std::vector<int>& arr, int threshold) {
    std::vector<int> result; // Вектор для хранения результатов

    // Перебираем каждый элемент входного массива
    for (int num : arr) {
        if (num > threshold) { // Проверяем, больше ли элемент порога
            result.push_back(num); // Добавляем элемент в результирующий вектор
        }
    }

    return result; // Возвращаем результирующий вектор
}

int main() {
    std::vector<int> input = {1, 5, 8, 3, 10};
    int threshold = 5;

    std::vector<int> filtered = filter_greater_than(input, threshold);

    std::cout << "Элементы больше " << threshold << ": ";
    for (int num : filtered) {
        std::cout << num << " "; // Выводим отфильтрованные элементы
    }
    std::cout << std::endl;

    return 0;
}#include <iostream>
#include <vector>

std::vector<int> filter_greater_than(const std::vector<int>& arr, int threshold) {
    std::vector<int> result; // Вектор для хранения результатов

    // Перебираем каждый элемент входного массива
    for (int num : arr) {
        if (num > threshold) { // Проверяем, больше ли элемент порога
            result.push_back(num); // Добавляем элемент в результирующий вектор
        }
    }

    return result; // Возвращаем результирующий вектор
}

int main() {
    std::vector<int> input = {1, 5, 8, 3, 10};
    int threshold = 5;

    std::vector<int> filtered = filter_greater_than(input, threshold);

    std::cout << "Элементы больше " << threshold << ": ";
    for (int num : filtered) {
        std::cout << num << " "; // Выводим отфильтрованные элементы
    }
    std::cout << std::endl;

    return 0;
}
