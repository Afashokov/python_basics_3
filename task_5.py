"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может
продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее
сумме и после этого завершить программу.
"""

# Вариант без использования пользовательских функций
# numbers_summ = 0  # сумма чисел, вынесен для избежания обнуления
# while True:
#     numbers_list = input('Введите нобор чисел через пробел или q для выхода >>> ').split()
#     counter = 0  # счетчик циклов
#     while counter < len(numbers_list):  # цикл удаляет из списка все не числовые элементы кроме q
#         if not numbers_list[counter].isdigit() and numbers_list[counter] != 'q':
#             numbers_list.pop(counter)  # выбран цикл while, так как for in "не любит" вмешательств в счетчик циклов
#             counter -= 1  # необходим в случае уделиния элемента, что бы проверить другой элемент с тем же индексом
#         counter += 1
#     for i in range(len(numbers_list)):
#         if numbers_list[i] != 'q':
#             numbers_summ += float(numbers_list[i])  # если использовать sum при наличии q, завершиться с ошибкой
#         elif numbers_list[i] == 'q':  # позволяет не обрабатывать числа после q
#             break  # чтобы обрабатывать все нужно закомментировать elif
#     print(f'Сумма введенных чисел: {numbers_summ}')
#     if 'q' in numbers_list:  # выход если q в списке
#         print('выход из программы')
#         exit()


def erase_not_numbers(numbers):
    counter_2 = 0  # счетчик циклов
    while counter_2 < len(numbers):  # цикл удаляет из списка все не числовые элементы кроме q
        if not numbers[counter_2].isdigit() and numbers[counter_2] != 'q':
            numbers.pop(counter_2)  # выбран цикл while, так как for in "не любит" вмешательств в счетчик циклов
            counter_2 -= 1  # необходим в случае уделиния элемента, что бы проверить другой элемент с тем же индексом
        counter_2 += 1
    return summator(numbers)  # функция возвращает результат другой функции


def summator(numbers):
    temp_result = 0
    for el in range(len(numbers)):
        if numbers[el] != 'q':
            temp_result += float(numbers[el])  # если использовать sum при наличии q, завершиться с ошибкой
        elif numbers[el] == 'q':  # позволяет не обрабатывать числа после q
            break  # чтобы обрабатывать все нужно закомментировать elif
    return temp_result


result = 0
while True:
    current_numbers = input('Введите нобор чисел через пробел или q для выхода >>> ').split()
    result += erase_not_numbers(current_numbers)
    print(f'Сумма чесел: {result}')
    if 'q' in current_numbers:
        print('Выход из программы.')
        exit()
