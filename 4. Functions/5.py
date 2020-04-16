#Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

print('Proszę o podane 3 różnych cyfr: ')
a = int(input('Proszę o podanie 1 cyfry: '))
b = int(input('Proszę o podanie 2 cyfry: '))
c = int(input('Proszę o podanie 3 cyfry: '))

def min():
    if a != b and a != c and c != b:
        if a < b and a < c:
            print(f'Najmniejsza liczba to {a}.')
        elif b < a and b < c:
            print(f'Najmniejsza liczba to {b}.')
        else:
            print(f'Najmniejsza cyfra to {c}.')
    else:
        print('Podano nieprawidłowe paramety.')

min()