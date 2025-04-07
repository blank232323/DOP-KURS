#include <iostream>
#include <vector>
#include <stdexcept> // Для std::runtime_error
#include <utility>   // Для std::pair

std::pair<int, int> find_min_max(const std::vector<int>& arr) {
    if (arr.empty()) {
        throw std::runtime_error("Ошибка: массив пуст."); // Генерируем исключение для пустого массива
    }

    int min_value = arr[0]; // Инициализируем минимальное значение первым элементом
    int max_value = arr[0]; // Инициализируем максимальное значение первым элементом

    // Перебираем элементы массива, начиная со второго
    for (size_t i = 1; i < arr.size(); ++i) {
        if (arr[i] < min_value) {
            min_value = arr[i]; // Обновляем минимальное значение
        }
        if (arr[i] > max_value) {
            max_value = arr[i]; // Обновляем максимальное значение
        }
    }

    return {min_value, max_value}; // Возвращаем пару значений
}

int main() {
    try {
        std::vector<int> input = {3, 5, 1, 8, -2, 7};
        auto [min_val, max_val] = find_min_max(input); // Деконструируем пару значений

        std::cout << "Минимальное значение: " << min_val << std::endl; // Ожидается -2
        std::cout << "Максимальное значение: " << max_val << std::endl; // Ожидается 8

        // Пример с пустым массивом
        std::vector<int> empty_input;
        find_min_max(empty_input); // Это вызовет исключение

    } catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl; // Выводим сообщение об ошибке
    }

    return 0;
}
