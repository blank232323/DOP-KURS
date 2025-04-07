class Stack:
    def __init__(self, size=10):
        self.size = size  # Максимальный размер стека
        self.stack = [None] * self.size  # Инициализация массива фиксированного размера
        self.top_index = -1  # Индекс верхнего элемента стека

    def push(self, value):
        """Добавление элемента в стек."""
        if self.top_index >= self.size - 1:
            print("Ошибка: стек переполнен.")
            return
        self.top_index += 1
        self.stack[self.top_index] = value

    def pop(self):
        """Удаление элемента из стека и возвращение его значения."""
        if self.is_empty():
            print("Ошибка: стек пуст.")
            return None
        value = self.stack[self.top_index]
        self.stack[self.top_index] = None  # Очистка значения
        self.top_index -= 1
        return value

    def top(self):
        """Возвращение элемента на вершине стека без удаления."""
        if self.is_empty():
            print("Ошибка: стек пуст.")
            return None
        return self.stack[self.top_index]

    def is_empty(self):
        """Проверка, пуст ли стек."""
        return self.top_index == -1

# Пример использования стека
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Вершина стека:", stack.top())  # Ожидается 3

    print("Удаленный элемент:", stack.pop())  # Ожидается 3
    print("Вершина стека после pop:", stack.top())  # Ожидается 2

    while not stack.is_empty():
        print("Удаленный элемент:", stack.pop())

    stack.pop()  # Ожидается сообщение об ошибке, так как стек пуст.
