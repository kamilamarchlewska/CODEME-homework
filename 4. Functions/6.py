# Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

print('Proszę o podane 3 różnych cyfr: ')
a = int(input('Proszę o podanie 1 cyfry: '))
b = int(input('Proszę o podanie 2 cyfry: '))
c = int(input('Proszę o podanie 3 cyfry: '))

def max():
    if a != b and a != c and c != b:
        if a > b and a > c:
            print(f'Największa liczba to {a}.')
        elif b > a and b > c:
            print(f'Największa liczba to {b}.')
        else:
            print(f'Największa cyfra to {c}.')
    else:
        print('Podano nieprawidłowe paramety.')

max()