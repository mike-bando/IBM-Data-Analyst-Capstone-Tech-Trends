# name = input("type in your first name: ")
# last_name = input("what's your last name?: ")
# age = int(input("what's your age?: "))
# float_number =float(input("type any floating number: "))
#
#
# print(f"your name is {name.upper()}, your last name is {last_name.lower()}")
# print(f"your age is {age}, your chosen floating number is {round(float_number,2)}")
#
# age+=1
# print('')
# print(f"In 1 year you'll be {age} years old")
from os import replace

#________________________________
# dlugosc = 0
# szerokosc = 0
# powierzchnia = 0
#
# while True:
#     try:
#         dlugosc = float(input("podaj dlugosc prostokata (w cm): "))
#         szerokosc = float(input("podaj szerokosc prostokata (w cm): "))
#
#
#         if dlugosc <0:
#             print("dlugosc nie moze byc mniejsza niz 0")
#         elif szerokosc <0:
#             print('szerokosc nie moze byc mniejsza niz 0')
#         else:
#             break
#     except ValueError:
#         print("to nie jest prawidlowa liczba")
#
# powierzchnia = dlugosc * szerokosc
#
#
# if powierzchnia >= 10000:
#     print(f"powierzchnia prostokatu o dlugosci rownej {dlugosc}cm i szerokosci rownej {szerokosc}cm wynosi razem: {powierzchnia/100} m2")
# else:
#     print(f"powierzchnia prostokatu o dlugosci rownej {dlugosc}cm i szerokosci rownej {szerokosc}cm wynosi razem: {powierzchnia} cm2")
#


#________________________________
# import math


# x = float(input("wpisz liczbe: "))
# x = 1
# y = 5
# z = 3.15
#
# result = abs(x)
# max_result = max(x,y,z)
# # print(round(result,5))
#
# # print(max_result)
# print(f"Pi = ", math.pi)
#

# c = pierwiastek z a^2 + b^2


# a = float(input("podaj a: "))
# b = float(input("podaj b: "))
#
# c = (round(math.sqrt((pow(a,2)+pow(b,2))),2))
#
# print(f"c = {c}")

#________________________________

# if statement


# age = int(input("podaj swoj wiek: "))
#
# if age >= 18:
#     print('mozesz aplikowac o karte kredytowa')
# else:
#     print('jestes zbyt mlody na karte kredytowa')
#
#
#

# odpowiedz = input('chcialbys cos zjesc? (Y/N): ')
# if odpowiedz.lower() == "y":
#     print('okej, to co zjemy?')
#     decyzja = input('na co masz ochote?: ')
#     print(f'dobrze, niech bedzie {decyzja}')
# elif odpowiedz.lower() == 'n':
#     print('okej, szkoda, bo ja jestem glodny')
# else:
#     print('zla odpowiedz')
#
#
# a = float(input('podaj liczbe a: '))
# b = float(input('podaj liczbe b: '))
# wynik = 0
# wybor = input('masz wybor dzialan podstawowych: wpisz dana opcje (+), (-), (*), (/), (everything): ')
# if wybor == "+":
#     wynik = a+b
#     print(f"wynik dodawania liczb {a} i {b} to: {wynik}")
# elif wybor == "-":
#     wynik = a - b
#     print(f"wynik odejmowania liczb {a} i {b} to: {wynik}")
# elif wybor == "*":
#     wynik = a * b
#     print(f"wynik mnozenia liczb {a} i {b} to: {wynik}")
# elif wybor == "/":
#     wynik = a / b
#     print(f"wynik dzielenia liczb {a} i {b} to: {wynik}")
# elif wybor == "everything":
#     wynik = a+b
#     wynik1 = a-b
#     wynik2 = a*b
#     wynik3 = a/b
#     print(f"podane liczby:\na: {a},\nb: {b},\n\nwynik dodawania: {wynik},\nwynik odejmowania: {wynik2},\nwynik mnozenia: {wynik3},\nwynik dzielenia: {wynik3}")
#
# else:
#     print('nie ma takiej opcji.')
#

#________________________________
# wartosc = int(input('podaj wage do przeliczenia: '))
# typ = input('kilogramy czy funty? (kg / lb): ')
#
#
# wynik = 0
# if typ == 'kg':
#     wynik = round(wartosc * 2.204,2)
#     print(f'waga przeliczona z {wartosc} {typ} = {wynik} lb')
#
# elif typ == 'lb':
#     wynik = round(wartosc / 2.204,2)
#     print(f'waga przeliczona z {wartosc} {typ} = {wynik} kg')
# elif typ != 'kg' or typ != 'lb':
#     print(f'wprowadzono {typ} - jest to nieprawidlowa wartosc')
# elif wartosc >0:
#     print('wprowadzona waga jest ponizej 0')
#
# else:
#     print('wprowadzona wartosc jest nieprawdziwa')
#
# #________________________________
#
# wartosc = int(input('podaj temperature do przeliczenia: '))
# typ = input('Celsius czy Fahrenheit? (C / F): ')
#
#
# wynik = 0
# if typ.lower() == 'c':
#     wynik = round((wartosc *1.8)+32,2)
#     print(f'Temperatura przeliczona z {wartosc} {typ.upper()} = {wynik} F')
#
# elif typ.lower() == 'f':
#     wynik = round((wartosc -32)/1.8,2)
#     print(f'Temperatura przeliczona z {wartosc} {typ.upper()} = {wynik} C')
# elif typ != 'kg' or typ != 'lb':
#     print(f'wprowadzono {typ} - jest to nieprawidlowa wartosc')
#
# else:
#     print('wprowadzona wartosc jest nieprawdziwa')
#

#________________________________

# temp = 5
# is_raining = True
#
# if temp > 35 or temp < 0 or is_raining:
#     print ('the outdoor event is cancelled')
# else:
#     print ("the outdoor event is still on")
#
#
#
#


# name = input('enter your full name: ')
#
# result = len(name)
# result = name.lower().find('a')
# name = name.capitalize()
# name = name.upper()

# print(name)
# print(result)
# phone_number = input("podaj nr telefonu: ")
#
# counter = phone_number.count('-')
# replacement_number = phone_number.replace('-', '...')
#
# print(phone_number)
# print(f'ilosc - w podanym numerze: {counter}')
# print(f"zamieniony nr telefonu: {replacement_number}")
#
#

# username = input('podaj swoje haslo: ')
# dlugosc = len(username)
#
# if dlugosc > 12:
#     print('Ilosc znakow jest za dluga, prosze podac haslo krotsze niz 12 znakow')
#     username = input('podaj jeszcze raz haslo: ')
# elif username.count(' ') > 0:
#     print("Haslo nie moze posiadac spacji.")
#     username = input('podaj jeszcze raz haslo: ')
# elif not username.isalpha():
#     print('haslo nie moze posiadac cyfr')
#     username = input('podaj jeszcze raz haslo: ')
# else:
#     print('podales dobre haslo')



#---------------------
# credit_number = "1234-5678-9012-3456-7890"
# #
# # print(credit_number[0:5])
# # print(credit_number[::5])
# # print(credit_number[-4:])
#
# credit_number = credit_number[::-1]
# print(credit_number)
#
# price1 = 3590.14159
# price2 = -9874.65
# price3 = 1231.34
#
# print(f"Price1 = ${price1:>10,.2f}")
# print(f"Price2 = ${price2:>10,.2f}")
# print(f"Price3 = ${price3:>10,.2f}")
#
#
# ------------------------

#
# age = int(input('Enter your age: '))
#
# while age < 0:
#     print("Age can't be less or equal to 0")
#     age =int(input('Enter your age: '))
# else:
#     print(f"your age is {age}")
#
#
# import random
#
#
# correct_number = random.randint(0,100)
# guess_number = int(input("podaj liczbe z przedzialu 0-100: "))
# while guess_number != correct_number:
#     if guess_number > correct_number:
#         print("Wybrany numer jest wyższy niż szczęśliwy numer")
#         guess_number = int(input("podaj jeszcze raz liczbe z przedzialu 0-100: "))
#         print('')
#     elif guess_number < correct_number:
#         print("Wybrany numer jest niższy niż szczęśliwy numer")
#         guess_number = int(input("podaj raz jeszcze liczbe z przedzialu 0-100: "))
#         print('')
#     else:
#         print('podany numer nie jest z przedziału 0-100')
#         guess_number = int(input("podaj liczbe z przedzialu 0-100: "))
#         print('')
# else:
#     print("Podałeś szczęśliwy numer, gratulacje!")



# credit_card = "1234-5678-9012-3456"
#
# for x in credit_card:
#     print(x)
#
#


import time
import sys

my_time = int(input('enter the time in seconds: '))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x / 3600)

    print(f'{hours:02}:{minutes:02}:{seconds:02}', end='\r', flush = True)
    time.sleep(1)

print("time's up!"             )












