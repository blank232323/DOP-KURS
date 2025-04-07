#include <iostream>
#include <string>
#include <set>

int count_unique_chars(const std::string& str) {
    std::set<char> unique_chars; // Множество для хранения уникальных символов

    // Перебираем каждый символ в строке
    for (char c : str) {
        unique_chars.insert(c); // Добавляем символ в множество
    }

    // Возвращаем количество уникальных символов
    return unique_chars.size();
}

int main() {
    std::string input = "hello";
    int unique_count = count_unique_chars(input);
    
    std::cout << "Количество уникальных символов в строке \"" << input << "\": " << unique_count << std::endl; // Ожидается 4

    return 0;
}
