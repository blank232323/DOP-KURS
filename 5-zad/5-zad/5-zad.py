#include <iostream>
#include <iomanip> // Для std::setw и std::setfill
#include <string>

void convert_to_12_hour_format(int hours, int minutes) {
    // Проверяем корректность входных данных
    if (hours < 0 || hours > 23 || minutes < 0 || minutes > 59) {
        std::cerr << "Ошибка: некорректное время." << std::endl;
        return;
    }

    std::string period = (hours >= 12) ? "PM" : "AM"; // Определяем AM или PM
    int converted_hours = hours % 12; // Конвертируем часы в 12-часовой формат

    // Если часы равны 0, то это 12 AM
    if (converted_hours == 0) {
        converted_hours = 12;
    }

    // Выводим результат с ведущим нулем для минут
    std::cout << converted_hours << ":" << std::setw(2) << std::setfill('0') << minutes << " " << period << std::endl;
}

int main() {
    convert_to_12_hour_format(14, 30); // Ожидается "2:30 PM"
    convert_to_12_hour_format(0, 45);   // Ожидается "12:45 AM"
    convert_to_12_hour_format(12, 15);  // Ожидается "12:15 PM"
    convert_to_12_hour_format(11, 59);  // Ожидается "11:59 AM"
    
    return 0;
}
