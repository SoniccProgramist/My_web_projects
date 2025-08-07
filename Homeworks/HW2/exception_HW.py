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
# print(get_element([1, 2, 3], 5)
