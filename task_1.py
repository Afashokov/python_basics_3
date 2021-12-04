"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def func_division(divisible, divider):
    """
    Возвращает результат деления
    :param divisible: делимое число
    :param divider: делитель
    :return: результат деления
    """
    try:
        return divisible / divider
    except ZeroDivisionError:
        print('Ошибка: деление на ноль')


# print(round(func_division(float(input('Введите дилимое число >>> ')), float(input('Введите делитель >>> '))), 3))

# 2-й вариант

numbers_list = input('Введите делимое число и делитель через запятую >>> ').split(',')
print(round(func_division(float(numbers_list[0]), float(numbers_list[1])), 2))
