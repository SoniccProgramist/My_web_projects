# рекурсия
# def outer_function(message):
#     def inner_function():
#         print(message)
#     return inner_function
#
# nihad_sleeps = outer_function("I was sleep 1 hour(")
# nihad_sleeps()
#декоратор
# def my_decorator(func):
#     def wrapper():
#         print('heyyyyyyyy')
#         func()
#         print('heyyyyyyyy')
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print('hello')
#
# say_hello()
# def decorator_with_arg(arg1, arg2):
#     def actual_decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f"Decoator = {arg1},{arg2}")
#             func(*args, **kwargs)
#         return wrapper
#     return actual_decorator
#
# @decorator_with_arg("Nihao", 3.14341234)
# def my_func(*args, **kwargs):
#     print("Function is done!")
#     print(args)
#     print(kwargs)
#
# my_func("m", 32, name="Nihad", age=45)

# import functools
#
# def decorator_with_arg(command):
#     """Dec params"""
#     init_dict = {}
#     def actual_decorator(func):
#         """Actual decorator"""
#         @functools.wraps(func)
#         def wrapper():
#             """Wrapper"""
#             # print(f"Decorator take arguments: {arg1}, {arg2}")
#             init_dict[command] = func
#             # func()
#         return wrapper
#     return actual_decorator
#
# @decorator_with_arg(command="start")
# def my_func():
#     """Main func"""
#     print("Function is done!")
#     # print(args)
#     # print(kwargs)
#
# # my_func()
#
# print(my_func.__name__)
# print(my_func.__doc__)

# import functools
# import time
# import datetime
# import random
#
# def simple_logger_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"[{datetime.datetime.now(). strftime('%H:%M:%S')}] Call function:  {func.__name__},")
#         result = func(*args, **kwargs)
#         print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Call function:  {func.__name__} end processing")
#         return result
#     return wrapper
# @simple_logger_decorator
# def add_number(digit1, digit2):
#     print(f"add digits: {digit1}+{digit2}")
#     return digit1 + digit2
#
# @simple_logger_decorator
# def sub_number(digit1, digit2):
#     print(f"add digits: {digit1}-{digit2}")
#     return digit1 - digit2
#
# add_number(37, 73)
# print(30 * '-')
# sub_number(102, 45)

def type_checker(...):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Логіка перевірки типів
            return func(*args, **kwargs)
        return wrapper
    return decorator
@type_checker(str, int)
def create_user(username, age):
    print(f"Створено користувача: {username}, Вік: {age}")
    return {"username": username, "age": age}

@type_checker(list, float)
def process_data_list(data, factor):
    print(f"Обробка списку: {data} з коефіцієнтом {factor}")
    return [x * factor for x in data]

print("Тестування Завдання 1:")
create_user("Олена", 25)
create_user(123, "Ігор") # Має викликати попередження/помилку
process_data_list([1.0, 2.0], 2.5)
process_data_list("не список", 1.0) # Має викликати попередження/помилку

import functools


def type_checker(*expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Логіка перевірки типів
            if len(args) == len(expected_types):

                for i in range(len(args)):
                    if not isinstance(args[i], expected_types[i]):
                        return None

                return func(*args, **kwargs)

            else:
                print("Something went wrong")

        return wrapper

    return decorator


@type_checker(str, int)
def create_user(username, age):
    print(f"Створено користувача: {username}, Вік: {age}")
    return {"username": username, "age": age}


@type_checker(list, float)
def process_data_list(data, factor):
    print(f"Обробка списку: {data} з коефіцієнтом {factor}")
    return [x * factor for x in data]


print("Тестування Завдання 1:")
create_user("Олена", 25)
create_user(123, "Ігор")
process_data_list([1.0, 2.0], 2.5)
process_data_list("не список", 1.0)