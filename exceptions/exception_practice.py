# Напишіть функцію `get_positive_integer()`, яка просить користувача ввести ціле число.
# Використайте `try-except` для обробки `ValueError`, якщо введено не число,
# та `TypeError`, якщо введено від'ємне число. Повторюйте запит, доки не отримаєте валідне додатне число.
# def get_positive_integer():
#     while True:
#         try:
#             num = int(input("Введіть ціле додатне число: "))
#             if num <= 0:
#                 print("Число має бути більше нуля!")
#             else:
#                 return num
#         except ValueError:
#             print("Це не ціле число!")
#         except TypeError:
#             print("Неправильний тип даних!")
#
# n = get_positive_integer()
# print("Ви ввели число:", n)
def get_positiv_integer():
    while True:
        try:
            num = int(input('ввести ціле число'))
            if num < 0:
                raise TypeError
            return num
        except ValueError:
            print("це не ціле число")
        except TypeError:
            print("це від'ємне число")

m = get_positiv_integer()
print("ви ввели число:", m)