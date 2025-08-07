# Маленькое задание:
# Напиши код, который:
#
# Спрашивает у пользователя число
#
# Если оно меньше нуля — вызывает исключение с текстом "Отрицательные значения запрещены"
#
# Иначе — просто печатает "Всё хорошо!"
# try:
#     x = input("Введите один символ: ")
#     if len(x) != 1 or x.isalpha() == False:
#         raise ValueError("Нужно ввести только одну букву.")
#     print("Всё хорошо!")
# except ValueError as e:
#     print("Ошибка:", e)

# def check_age(age):
#     if 0 > age or age > 120:
#         raise ValueError("Возраст указан неверно!")
#     else:
#         return "Возраст принят"
#
# try:
#     age = int(input("Введите возраст: "))
#     result = check_age(age)
#     print(result)
# except ValueError as e:
#     print("Error:", e)

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[Ошибка в {func.__name__}]: {e}")
    return wrapper

@catch_errors
def divide(a, b):
    return a / b

@catch_errors
def parse_int(text):
    return int(text)

#print(divide(10, 0))      # ZeroDivisionError
#print(parse_int("abc"))   # ValueError

@catch_errors
def get_items(lst, index):
    if index >= len(lst):
        raise IndexError("Неверный индекс!")
    else:
        return lst[index]

my_list = [10, 20, 30]
print(get_items(my_list, 1))  # => 20
print(get_items(my_list, 10))

# Створіть декоратор @check_division_error, який перевіряє, чи немає ділення на нуль в функціях. Якщо при виклику функції сталася помилка ділення на нуль, декоратор повинен вивести повідомлення про помилку та завершити виконання програми.
# Створіть декоратор @check_index_error, який перевіряє, чи виходить індекс за межі списку при доступі до елементу. Якщо при виклику функції сталася помилка індексації, декоратор повинен вивести повідомлення про помилку та завершити виконання програми.
# Створіть функцію divide, яка приймає два числа a та b і повертає результат ділення a на b. Додайте декоратор @check_division_error до цієї функції.
# Створіть функцію get_element, яка приймає список lst та індекс idx і повертає елемент зі списку за вказаним індексом. Додайте декоратор @check_index_error до цієї функції.
# Напишіть кілька тестових випадків для кожної з функцій divide та get_element, включаючи ситуації, де можуть виникнути помилки.
# Перевірте роботу декораторів та функцій, запустивши тести.
# У випадку виявлення помилок, переконайтеся, що декоратори виводять відповідні повідомлення та завершають виконання програми.
# Закінчіть завдання, надславши код декораторів та тестів.
# Це завдання дозволить перевірити навички створення та використання декораторів для перевірки коду на можливі помилки.
import sys
def check_division_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print(f"У функції {func.__name__} сталася помилка ділення на нуль")
            sys.exit("Програма завершена.")
    return wrapper

def check_index_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print(f"У функції {func.__name__} індекс виходить за межі списку при доступі до елементу")
            sys.exit("Програма завершена.")
    return wrapper

@check_division_error
def divide(num1, num2):
    return num1 / num2

@check_index_error
def get_element(lst, index):
    return lst[index]

# print("Тест 1: divide(10, 2)")
# print(divide(10, 2))
#
# print("Тест 2: divide(5, 0)")
# print(divide(5, 0))
#
# print("Тест 3: get_element([1, 2, 3], 1)")
# print(get_element([1, 2, 3], 1))
#
# print("Тест 4: get_element([1, 2, 3], 5)")
# print(get_element([1, 2, 3], 5))
