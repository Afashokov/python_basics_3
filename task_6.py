"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

text_sample = 'text'
text_string = 'this is a sample text it should not mean anything'
user_input = input('Ввидите строку из слов, разделенных пробелом >>> ')

print('Пример 1. Метод title')


def int_func(text):
    return text.title()


print(text_sample)
print(int_func(text_sample))
print(text_string)
print(int_func(text_string))
print(int_func(user_input))

print('Пример 2. Метод capitalize и цикл for in')


def int_func_2(text):
    if ' ' in text:
        text = text.split()
        for el in range(len(text)):
            text[el] = text[el].capitalize()
        text = ' '.join(text)
    else:
        text = text.capitalize()
    return text


print(text_sample)
print(int_func_2(text_sample))
print(text_string)
print(int_func_2(text_string))
print(int_func_2(user_input))

print('Пример 3. Методы upper, lower и несколько циклов for in')


def int_func_3(text):
    if ' ' in text:
        text = text.split()
        for element in text:
            temp_word = ''
            for i in element:
                temp_word += ' ' + i
            temp_word = temp_word.split()
            for p in range(len(temp_word)):
                if p == 0:
                    temp_word[0] = temp_word[0].upper()
                else:
                    temp_word[p] = temp_word[p].lower()
            text[text.index(element)] = ''.join(temp_word)
        text = ' '.join(text)
    else:
        temp_word = ''
        for i in text:
            temp_word += ' ' + i
        text = temp_word
        text = text.split()
        for p in range(len(text)):
            if p == 0:
                text[0] = text[0].upper()
            else:
                text[p] = text[p].lower()
        text = ''.join(text)
    return text


print(text_sample)
print(int_func_3(text_sample))
print(text_string)
print(int_func_3(text_string))
print(int_func_3(user_input))
