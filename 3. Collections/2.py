#Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste

list = []

for i in range(10):
    i = int(input('Proszę o podanie cyfry:'))
    i = round(i)
    if i % 2 != 0:
        list.append(i)

print('Podane listy nieparzyste to:', list)