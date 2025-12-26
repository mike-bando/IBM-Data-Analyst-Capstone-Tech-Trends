# # yield - dostarczyc, dac, wydac z siebie


# def generate_even_numbers():
#     print('start')
#     for element in range(400):
#         if element % 2 == 0:
#             print('\nprzed yield')
#             yield element
#             print('po yield\n')
#             print("-" * 20)



# evenNumbersGenerator = (element for element in range(400)
#                         if element %2 == 0)

# # a = generate_even_numbers()
# # print("-" * 20)

# # print(f"Zwrócona wartość: {next(a)}")

# # print(f"Zwrócona wartość: {next(a)}")
# # print(f"Zwrócona wartość: {next(a)}")

# def generate_10_numbers():
#     x = 0
#     while x < 10:
#         yield x
#         x += 1 

# liczby = generate_10_numbers()

# print('krok 1:',next(liczby))
# print('krok 2:',next(liczby))
# print('krok 3:',next(liczby))
# print('krok 4:',next(liczby))
# print('krok 5:',next(liczby))

# print('krok 6:',next(liczby))
# print('krok 7:',next(liczby))
# print('krok 8:',next(liczby))
# print('krok 9:',next(liczby))
# print('krok 10(ostatni):',next(liczby))

# try:
#     print(next(liczby))
# except:
#     print('Wiecej sie nie da, petla while sie zakonczyla')


# def number_generator():
#     number = 0 
#     while True:
#         # number += 1
#         number = yield number * number


# generatedNumbers = []

# numberGenerator = number_generator()

# # for _ in range(20):
# #     generatedNumbers.append(next(numberGenerator))

# # print(generatedNumbers)



# # for _ in range(30):
# #     generatedNumbers.append(next(numberGenerator))

# # print(generatedNumbers)
# next(numberGenerator) #pierwszy next do uruchomienia generatora, pozniej mozna podac argument przy .send()

# print(numberGenerator.send(5)) #send pozwala podac argument do zrobienia z tego liczby ^2ł


# number_generator(5)

