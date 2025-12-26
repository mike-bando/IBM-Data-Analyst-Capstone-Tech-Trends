import requests

# To jest publiczne, darmowe API z danymi o "zadaniach do zrobienia"
url = "https://jsonplaceholder.typicode.com/todos/1"

print("Wysyłam zapytanie...")

# Tu nie potrzebujemy headers, bo to publiczne dane
response = requests.get(url)

if response.status_code == 200:
    print("SUKCES! (Kod 200)")
    data = response.json()
    print("Otrzymane dane:")
    print(data)
else:
    print(f"Błąd: {response.status_code}")