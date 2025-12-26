# # name = input("type in your first name: ")
# # last_name = input("what's your last name?: ")
# # age = int(input("what's your age?: "))
# # float_number =float(input("type any floating number: "))
# #
# #
# # print(f"your name is {name.upper()}, your last name is {last_name.lower()}")
# # print(f"your age is {age}, your chosen floating number is {round(float_number,2)}")
# #
# # age+=1
# # print('')
# # print(f"In 1 year you'll be {age} years old")
# # from os import replace

# #________________________________
# # dlugosc = 0
# # szerokosc = 0
# # powierzchnia = 0
# #
# # while True:
# #     try:
# #         dlugosc = float(input("podaj dlugosc prostokata (w cm): "))
# #         szerokosc = float(input("podaj szerokosc prostokata (w cm): "))
# #
# #
# #         if dlugosc <0:
# #             print("dlugosc nie moze byc mniejsza niz 0")
# #         elif szerokosc <0:
# #             print('szerokosc nie moze byc mniejsza niz 0')
# #         else:
# #             break
# #     except ValueError:
# #         print("to nie jest prawidlowa liczba")
# #
# # powierzchnia = dlugosc * szerokosc
# #
# #
# # if powierzchnia >= 10000:
# #     print(f"powierzchnia prostokatu o dlugosci rownej {dlugosc}cm i szerokosci rownej {szerokosc}cm wynosi razem: {powierzchnia/100} m2")
# # else:
# #     print(f"powierzchnia prostokatu o dlugosci rownej {dlugosc}cm i szerokosci rownej {szerokosc}cm wynosi razem: {powierzchnia} cm2")
# #


# #________________________________
# # import math


# # x = float(input("wpisz liczbe: "))
# # x = 1
# # y = 5
# # z = 3.15
# #
# # result = abs(x)
# # max_result = max(x,y,z)
# # # print(round(result,5))
# #
# # # print(max_result)
# # print(f"Pi = ", math.pi)
# #

# # c = pierwiastek z a^2 + b^2


# # a = float(input("podaj a: "))
# # b = float(input("podaj b: "))
# #
# # c = (round(math.sqrt((pow(a,2)+pow(b,2))),2))
# #
# # print(f"c = {c}")

# #________________________________

# # if statement


# # age = int(input("podaj swoj wiek: "))
# #
# # if age >= 18:
# #     print('mozesz aplikowac o karte kredytowa')
# # else:
# #     print('jestes zbyt mlody na karte kredytowa')
# #
# #
# #

# # odpowiedz = input('chcialbys cos zjesc? (Y/N): ')
# # if odpowiedz.lower() == "y":
# #     print('okej, to co zjemy?')
# #     decyzja = input('na co masz ochote?: ')
# #     print(f'dobrze, niech bedzie {decyzja}')
# # elif odpowiedz.lower() == 'n':
# #     print('okej, szkoda, bo ja jestem glodny')
# # else:
# #     print('zla odpowiedz')
# #
# #
# # a = float(input('podaj liczbe a: '))
# # b = float(input('podaj liczbe b: '))
# # wynik = 0
# # wybor = input('masz wybor dzialan podstawowych: wpisz dana opcje (+), (-), (*), (/), (everything): ')
# # if wybor == "+":
# #     wynik = a+b
# #     print(f"wynik dodawania liczb {a} i {b} to: {wynik}")
# # elif wybor == "-":
# #     wynik = a - b
# #     print(f"wynik odejmowania liczb {a} i {b} to: {wynik}")
# # elif wybor == "*":
# #     wynik = a * b
# #     print(f"wynik mnozenia liczb {a} i {b} to: {wynik}")
# # elif wybor == "/":
# #     wynik = a / b
# #     print(f"wynik dzielenia liczb {a} i {b} to: {wynik}")
# # elif wybor == "everything":
# #     wynik = a+b
# #     wynik1 = a-b
# #     wynik2 = a*b
# #     wynik3 = a/b
# #     print(f"podane liczby:\na: {a},\nb: {b},\n\nwynik dodawania: {wynik},\nwynik odejmowania: {wynik2},\nwynik mnozenia: {wynik3},\nwynik dzielenia: {wynik3}")
# #
# # else:
# #     print('nie ma takiej opcji.')
# #

# #________________________________
# # wartosc = int(input('podaj wage do przeliczenia: '))
# # typ = input('kilogramy czy funty? (kg / lb): ')
# #
# #
# # wynik = 0
# # if typ == 'kg':
# #     wynik = round(wartosc * 2.204,2)
# #     print(f'waga przeliczona z {wartosc} {typ} = {wynik} lb')
# #
# # elif typ == 'lb':
# #     wynik = round(wartosc / 2.204,2)
# #     print(f'waga przeliczona z {wartosc} {typ} = {wynik} kg')
# # elif typ != 'kg' or typ != 'lb':
# #     print(f'wprowadzono {typ} - jest to nieprawidlowa wartosc')
# # elif wartosc >0:
# #     print('wprowadzona waga jest ponizej 0')
# #
# # else:
# #     print('wprowadzona wartosc jest nieprawdziwa')
# #
# # #________________________________
# #
# # wartosc = int(input('podaj temperature do przeliczenia: '))
# # typ = input('Celsius czy Fahrenheit? (C / F): ')
# #
# #
# # wynik = 0
# # if typ.lower() == 'c':
# #     wynik = round((wartosc *1.8)+32,2)
# #     print(f'Temperatura przeliczona z {wartosc} {typ.upper()} = {wynik} F')
# #
# # elif typ.lower() == 'f':
# #     wynik = round((wartosc -32)/1.8,2)
# #     print(f'Temperatura przeliczona z {wartosc} {typ.upper()} = {wynik} C')
# # elif typ != 'kg' or typ != 'lb':
# #     print(f'wprowadzono {typ} - jest to nieprawidlowa wartosc')
# #
# # else:
# #     print('wprowadzona wartosc jest nieprawdziwa')
# #

# #________________________________

# # temp = 5
# # is_raining = True
# #
# # if temp > 35 or temp < 0 or is_raining:
# #     print ('the outdoor event is cancelled')
# # else:
# #     print ("the outdoor event is still on")
# #
# #
# #
# #


# # name = input('enter your full name: ')
# #
# # result = len(name)
# # result = name.lower().find('a')
# # name = name.capitalize()
# # name = name.upper()

# # print(name)
# # print(result)
# # phone_number = input("podaj nr telefonu: ")
# #
# # counter = phone_number.count('-')
# # replacement_number = phone_number.replace('-', '...')
# #
# # print(phone_number)
# # print(f'ilosc - w podanym numerze: {counter}')
# # print(f"zamieniony nr telefonu: {replacement_number}")
# #
# #

# # username = input('podaj swoje haslo: ')
# # dlugosc = len(username)
# #
# # if dlugosc > 12:
# #     print('Ilosc znakow jest za dluga, prosze podac haslo krotsze niz 12 znakow')
# #     username = input('podaj jeszcze raz haslo: ')
# # elif username.count(' ') > 0:
# #     print("Haslo nie moze posiadac spacji.")
# #     username = input('podaj jeszcze raz haslo: ')
# # elif not username.isalpha():
# #     print('haslo nie moze posiadac cyfr')
# #     username = input('podaj jeszcze raz haslo: ')
# # else:
# #     print('podales dobre haslo')



# #---------------------
# # credit_number = "1234-5678-9012-3456-7890"
# # #
# # # print(credit_number[0:5])
# # # print(credit_number[::5])
# # # print(credit_number[-4:])
# #
# # credit_number = credit_number[::-1]
# # print(credit_number)
# #
# # price1 = 3590.14159
# # price2 = -9874.65
# # price3 = 1231.34
# #
# # print(f"Price1 = ${price1:>10,.2f}")
# # print(f"Price2 = ${price2:>10,.2f}")
# # print(f"Price3 = ${price3:>10,.2f}")
# #
# #
# # ------------------------

# #
# # age = int(input('Enter your age: '))
# #
# # while age < 0:
# #     print("Age can't be less or equal to 0")
# #     age =int(input('Enter your age: '))
# # else:
# #     print(f"your age is {age}")
# #
# #
# # import random
# #
# #
# # correct_number = random.randint(0,100)
# # guess_number = int(input("podaj liczbe z przedzialu 0-100: "))
# # while guess_number != correct_number:
# #     if guess_number > correct_number:
# #         print("Wybrany numer jest wyższy niż szczęśliwy numer")
# #         guess_number = int(input("podaj jeszcze raz liczbe z przedzialu 0-100: "))
# #         print('')
# #     elif guess_number < correct_number:
# #         print("Wybrany numer jest niższy niż szczęśliwy numer")
# #         guess_number = int(input("podaj raz jeszcze liczbe z przedzialu 0-100: "))
# #         print('')
# #     else:
# #         print('podany numer nie jest z przedziału 0-100')
# #         guess_number = int(input("podaj liczbe z przedzialu 0-100: "))
# #         print('')
# # else:
# #     print("Podałeś szczęśliwy numer, gratulacje!")



# # credit_card = "1234-5678-9012-3456"
# #
# # for x in credit_card:
# #     print(x)
# #
# #

# #### Timer w jednej linii
# # import time
# # import sys
# #
# # my_time = int(input('enter the time in seconds: '))
# #
# # for x in range(my_time, 0, -1):
# #     seconds = x % 60
# #     minutes = int(x/60) % 60
# #     hours = int(x / 3600)
# #
# #     print(f'{hours:02}:{minutes:02}:{seconds:02}         ', end='\r', flush = True)
# #     time.sleep(1)
# #
# # print("time's up!"             )
# #
# #
# #


# # fruits = ['apple', 'banana','orange','coconut']
# # fruits = ('apple', 'banana','orange','coconut')
# #
# # print(f'stara lista: ',fruits)
# # # print(help(fruits))
# # # iterator = iter(fruits)
# # # print(next(iterator))
# # # print(next(iterator))
# # # print(fruits.count('coconut'))
# #
# #
# #
# #
# # print(f"nowa lista: ", fruits)



# # owoce = ['banan','jablko','mandarynka','gruszka']
# # warzywa = ['seler','marchew','ziemniaki']
# # miesa = ['kurczak','ryba','indyk']
# #
# # # print(owoce,'\n',warzywa,'\n',miesa)
# #
# # zakupy = [owoce, warzywa, miesa]
# #
# # for produkt in zakupy:
# #     for x in produkt:
# #         print(x, end=' ')
# #     print('')
# #
# # # print(zakupy[2][0])

# # przyciski = ((1,2,3),
# #               (4,5,6),
# #               (7,8,9),
# #               ('*', 0, '#'))
# # for przycisk in przyciski:
# #     for x in przycisk:
# #         print(x, end=' ')
# #     print('')




# # capitals = {"USA":"Washington D.C.",
# #             "India":"Delphi",
# #             "China":"Pekin",
# #             "Poland":"Warsaw"}

# # print(capitals.get('Poland'))


# # -----------------------------------
# # import random

# # random_number = random.randint(1,20)


# # print(random_number)

# # options = ("rock","paper","scissors")
# # cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']



# # card = random.shuffle(cards)

# # option = random.choice(options)

# # # print(option)
# # print(cards)


# # -----------------------------------

# # def greetings(name, age):
# #     print(f'happy birthday to {name}!')
# #     print(f"You're getting older today! You've turned {age}, still long time to go.")


# # greetings("Michal", 30)

# # def display_invoice(username, amount, due_date):
# #     print(f'Hello {username}!')
# #     print(f'Your bill of ${amount:.2f} is due on {due_date}')


# # display_invoice("andrzej", 21.37, 9.11)

# # wynik = 0
# # wartosc1 = int(input("podaj value1: "))
# # wartosc2 = int(input("podaj value2: "))

# # def dodaj(value1, value2):
# #     wynik = value1+value2
# #     return wynik

# # print(dodaj(wartosc1, wartosc2))


# # def full_name(first, last):
# #     first = first.capitalize()
# #     last = last.capitalize()
# #     return first + " " + last

# # print(full_name("michal", "bando"))


# # def net_price(list_price, discount=0, tax=0.05): #Default argument - w funkcji wpisany odgornie

# #     return list_price * (1-discount)* (1+tax)


# #print(net_price(500))

# # print(net_price(500,0.1))

# # import time


# # def count(end, start = 0):
# #     for x in range(start, end+1):
# #         print(x)
# #         time.sleep(0.3)
# #     print('done!')


# # count(30,15)




# # def hello (greeting, title, first, last):
# #     print(f"{greeting} {title}{first} {last}")




# # hello ("hello", title="Mr.", first="Michal", last="Bando")


# # def get_phone_no(country, area, first, last):
# #     return f'{country}-{area}-{first}-{last}'




# # phone_num = get_phone_no(country="+48",area=886,first=953,last=424)

# # print(phone_num)


# # *args = allows you to pass multiple non-key arguments
# # **kwards = allow you to pass multiple keyword - arguments
# # * unpacking operator
# # 1. positional, 2. default, 3. keyword, 4. ARBITRARY


# # def add(*args):
# #     print(type(args))
          
          

# # a=(1,2,3,4,5,6,7,8)
# # total=0
    
# # for char in a:
# #     total += a [char-1]
# #     print(total)



# # def add(*args):
# #     total = 0
# #     for arg in args:
# #         total += arg
# #     return total

# # print(add(1,2,3,4,5,6,7,8))


# # def display_name(*args):
# #     for arg in args:
# #         print(arg, end=" ")

# # display_name("Michal","Adam","Bando")

# # def print_address(**kwargs):
# #     for key,value in kwargs.items():
# #         print(f"{key}:{value}")


# # print_address(street="Ogrodowa", city='Kalwaria', state="Malopolska", kod_pocztowy="34-130")

# # print(' ')
# # def shipping_label(*args, **kwargs):
# #     for arg in args:
# #         print(arg, end=" ")
# #     print("\n")
# #     for key, value in kwargs.items():
# #         print(f"{key:15}: {value}")

# # shipping_label("Mr",'Michal','Bando', 
# #                street="Ogrodowa",
# #                number = "25",
# #                city = "Kalwaria Zebrzydowska",
# #                voivodeship = "Malopolska",
# #                country='Polska')


# # numbers = (1,2,3,4,5,6,7,8,9,10)

# # for number in numbers:
# #     print(number)


# # fruits = {"apple","banana", "orange","coconut"}
# # for fruit in fruits:
# #     print(fruit)



# # name = "michal bando"

# # for char in name:
# #     print(char, end = ' ')




# # my_dictionary = {'A':1, 'B':2,'C':3}

# # for key, value in my_dictionary.items():
# #     print(f"{key}: {value}")
                                

# # -----------------------------------------




# # word = "APPLE"


# # letter = input("Guess a letter in the secret word: ")



# # if letter.upper() in word:
# #     print(f"there's a '{letter}' in a secret word")
# # else:
# #     print(f"{letter} was not found")



# # students = {"Spongebob","Patrick", "Sandy"}

# # student = input("Enter the name of the student: ")


# # if student not in students:
# #     print(f"{student} is not a student!")
# # else:
# #     print(f"{student} is a student.")


# # grades = {"Sandy":"A", "Squidward":"B", "Spongebob": "C", "Patrick": "D"}


# # student = input("Enter the name of a student: ")

# # if student in grades:
# #     print(f"{student} has a grade {grades[student]}")



# # email = "Bando.Michal@gmail.com"

# # if "@" in email and "." in email:
# #     print(f"{email} is a valid email")
# # else:
# #     print("not valid")


# # doubles = []
# # for x in range(1,11):
# #     doubles.append(x*2)

# # # print(doubles)
# # doubles = [x*2 for x in range(1,11)]
# # triples = [y*3 for y in range(1,11)]
# # squares = [z ** 2 for z in range (1,11)]
# # print(squares)


# # fruits = ['apple','orange','banana','coconut']
# # fruits_chars = [fruit[0] for fruit in fruits]
# # # print(fruits_chars)

# # numbers = [1,-2,3,-4,5,-6,8]

# # pos_nums = [number for number in numbers if number >= 0]
# # neg_nums = [number for number in numbers if number <= 0]
# # even_nums = [number for number in numbers if number % 2 == 0] 
# # odd_nums = [number for number in numbers if number % 2 == 1]

# # print(odd_nums)

# # grades = [85,15,50,59,60,61]

# # passed = [grade for grade in grades if grade >= 60]

# # print(passed)

# #-------------------------



# # match-case statement
# # alternative to use many elif statements


# # def is_weekend(day):
# #     match day:
# #         case "Sunday" | "Saturday":             # | = or
# #             return True
# #         case _:                                 # wildcard
# #             return "False"


# # print(is_weekend("Saturday"))


# #-------------------------

# # print(help("modules"))

# # import math
# # print(math.pi)

# # import math as m
# # print(m.pi)

# # from math import pi
# # print(pi)

# # import example

# # result = example.pi
# # result = example.square(3)
# # result = example.cube(3)
# # result = example.circumference(15)
# # result = example.area(5)
# # print(result)




# # -------------------------------
# # Order zmiennych:
# # LEGB = Local -> Enclosed -> Global -> Built-in


# # def func1():
# #     a = 1
# #     print(a)

# # def func2():
# #     b = 2
# #     print(b)

# # func1()
# # func2()

# # from math import e

# # def function1():
# #     print(e)

# # function1()




# # ----------------------------


# import random, string

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()



# random.shuffle(key)

# # print(f"chars: {chars}")
# # print(f"key: {key}")


# # ENCRYPTION
# plain_text = input("Enter a message to encrypt: ")
# cipher_text = ""

# for letter in plain_text:
#     index = key.index(letter)

#     cipher_text += chars[index]

# print(f"Original message: {plain_text}")
# print(f"Encrypted message: {cipher_text}")


# # DECRYPTION

# cipher_text = input("Enter a message to encrypt: ")
# plain_text = ""

# for letter in cipher_text:
#     index = chars.index(letter)

#     plain_text += key[index]

# print(f"Encrypted message: {cipher_text}")
# print(f"Decrypted message: {plain_text}")



# def add_sprinkles(funkcja):
#     print("***SPRINKLES***")
#     funkcja()



# def get_ice_cream():
#     print("Here's your ice cream!")

# get_ice_cream()


from datetime import datetime

start = datetime.now()
end = datetime(2025, 1, 7, 10, 15)

difference = end - start
hours = difference.total_seconds() / 3600

print(f"Liczba godzin: {hours}")