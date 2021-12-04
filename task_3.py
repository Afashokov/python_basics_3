"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

numbers_list = input('Введите 3 или больше (будут использованы 3 первых) числа через пробел>>> ').split()


def my_func(first_number, second_number, third_number):
    temp_list = [first_number, second_number, third_number]
    return sum(temp_list) - min(temp_list)


print('Способ 1')
print(my_func(50, 30, 30))
print(my_func(float(numbers_list[0]), float(numbers_list[1]), float(numbers_list[2])))


def my_func2(first_number, second_number, third_number):
    if first_number > third_number < second_number:
        return first_number + second_number
    elif first_number > second_number < third_number:
        return first_number + third_number
    else:
        return second_number + third_number


print('Способ 2')
print(my_func(50, 30, 30))
print(my_func2(float(numbers_list[0]), float(numbers_list[1]), float(numbers_list[2])))
