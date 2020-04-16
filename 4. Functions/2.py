#Napisać funkcję, która sprawdza czy liczba jest parzysta.

def even():
    number = int(input('Proszę o podanie liczby: '))
    p = number % 2
    if p == 0:
        print('Ta liczba jest parzysta.')
    else:
        print('Ta liczba jest nieparzysta.')

even()