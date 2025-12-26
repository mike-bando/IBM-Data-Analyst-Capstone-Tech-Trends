# # file = open('test.txt','w')

# # file.write('Sample')

# # file.close()

# try:
#     file = open('test.txt','w')
#     file.write('Sample1')

#     # print(0/0)
#     file.write('Sample2')
# finally:
#     file.close()

# with open('test.txt','w') as file:
#     file.write('sample123\n')
#     file.write('sample321\t')

# imiona_nazwiska = []
# imiona = []
# nazwiska = []
# with open('imionanazwiska1.txt','r') as file:
#     # imiona_nazwiska = file.write('Michal Bando\nRenata Dziedzic')
#     for line in file:
#         imiona_nazwiska.append(tuple(line.replace('\n','').split(' ')))

# print(imiona_nazwiska)
# # imiona_nazwiska[0].append(imiona)

# with open('imiona.txt','w') as file:
#     for imie in imiona_nazwiska:
#         file.write(imie[0]+'\n')

# with open('nazwiska.txt','w') as file:
#     for nazwisko in imiona_nazwiska:
#         file.write(nazwisko[1]+'\n')

# def read_content_of_file(path):
#     try:
#         with open(path, "r", encoding="UTF-8") as file:
#             return file.read()
#     except FileNotFoundError:
#          print("Nie znaleziono pliku, podaj prawidłową ścieżkę")
 
# nameOfFile = input("Podaj nazwę pliku do otwarcia: ")
 
# fileContent = read_content_of_file(nameOfFile)





# film = {
#     'title':'Tytul',
#     'release_year':'1991',
#     'won_oscar':True,
#     'actors':("Michal Bando",'Renata Dziedzic'),
#     'budget':None,
#     'credits':{
#         'director':'Imie Nazwisko',
#         'writer':'Ktos Inny',
#         'animator':'Ktos Jeszczeinny'
#     }
# }

# json.dumps(film, ensure_ascii=False)

# with open('sample.json','w', encoding='UTF-8') as file:
#     json.dump(film,file, ensure_ascii=False)

# jsonMovie = '{"title": "Tytul", "release_year": "1991", "won_oscar": true, "actors": ["Michal Bando", "Renata Dziedzic"], "budget": null, "credits": {"director": "Imie Nazwisko", "writer": "Ktos Inny", "animator": "Ktos Jeszczeinny"}}'


# encodedMovie = json.loads(jsonMovie)
# print(encodedMovie)

# with open('sample.json',encoding='UTF-8') as file:
#     encodedMovie = json.load(file)
# print(encodedMovie)
# # response = requests.get('http://videokurs.pl')
# print(' ')
# print(response)
# print(' ')

# print(response.history)

# program, ktory pobiera od uzytkownika strone internetowa *http://google.com*
# zapisuje w liscie (strony_statusy) polaczenie stron i statusow

# strony_statusy = []
# status = ''
# input_strony = ''
# dlugosc_listy = len(strony_statusy)
# def sprawdz_strony():
    
#     status = ''
#     input_strony = input('Podaj adres strony do sprawdzenia: ')
#     try:
#         status = requests.get(input_strony)
#         strony_statusy.append(input_strony)
#         print(status)
#         strony_statusy.append(status)
#     except:
#         print("Taka strona nie istnieje")
#     # strony_statusy
# while dlugosc_listy <5:
#     sprawdz_strony()
#     print(strony_statusy)
#     dlugosc_listy+=1
# else:
#     print(strony_statusy)
    

# print(strony_statusy)




import requests
import json
from collections import defaultdict #defaultdictionary to domyslny slownik - pozwala nam dodac cos do pustego slownika

r = requests.get('https://jsonplaceholder.typicode.com/todos')

def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()  # mozna uzyc defaultdict() aby ominac try/except z dodawaniem do pustego slownika 
    for entry in tasks:
        if entry['completed'] == True:
            try:
                completedTaskFrequencyByUser[entry['userId']] += 1 
            except KeyError:
                completedTaskFrequencyByUser[entry['userId']] = 1
    return completedTaskFrequencyByUser

def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTask = []
    maxAmountOfCompletedTasks = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items():
        if numberOfCompletedTasks == maxAmountOfCompletedTasks:
            usersIdWithMaxCompletedAmountOfTask.append(userId)

    return usersIdWithMaxCompletedAmountOfTask


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print('Niepoprawny format')
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
    print("Top id to: ", usersWithTopCompletedTasks)

r = requests.get('https://jsonplaceholder.typicode.com/users')

# users = r.json()

# for user in users:
#     if user['id'] in (usersWithTopCompletedTasks):
#         print(f"UserId: {user['id']} - {user['name']}")

r = requests.get('https://jsonplaceholder.typicode.com/')