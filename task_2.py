"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user_form(name, surname, birth_year, living_city, user_email, phone_number):
    print(f'name: {name}, surname: {surname}, year of birth: {birth_year},'
          f' city of residence: {living_city}, email: {user_email}, phone number: {phone_number}')


user_form(birth_year=1984, user_email='djohn@gmail.com', name='John', surname='Doe',
          phone_number='+1 (852) 777-55-33', living_city='New-York')

user_form(phone_number=input('input phone number >>> '), surname=input('input surname >>> '),
          birth_year=int(input('input year of birth >>> ')), name=input('input name >>> '),
          living_city=input('input city of residence >>> '), user_email=input('input email >>> '))


