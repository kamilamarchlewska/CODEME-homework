#Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def range_1 ():
    a = int(input('Proszę o podanie początkowego zakresu liczb: '))
    b = int(input('Proszę o podanie początkowego zakresu liczb: '))
    if a > 10 and 10 < b:
        print(f'nie, liczba 10 jest z poza zakresu')
    else:
        print(f'tak, liczba 10 znajduje się w zadanym zakresie')

range_1()