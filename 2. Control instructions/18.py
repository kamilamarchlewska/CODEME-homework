#Stwórz grę ciepło zimno.
#Komputer losuje liczbę z zakresu od 1 do 100.
#Użytkownik podaje swój traf.
#Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#Jeśli użytkownik zgadnie wygrywa gracz.
#Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

print('GRA CIEPŁO ZIMNO')
help = input('CZY CHCESZ ZAPOZNAĆ SIĘ Z ZASADAMI GRY? WPISZ TAK/NIE: ')

if help == 'TAK':
    print('''1. Przeciwnik losuje liczbę z zakresu od 1 do 100.
    2. Podajesz swój traf od 1 do 100. Masz 6 prób do wykorzystania.
    3. Przeciwnik odpowiada ciepło zimno.
    4. Jeżeli w ciągu 6 prób - wygrywasz :)
    5. Jeżeli nie uda Ci się zgadnąć - wygrywa przeciwnik.
    
ZACZYNAMY! ''')

else:
    print('')
    print('ZACZYNAMY!')

revenge = 'TAK'
while revenge == 'TAK':

    choice_comp = random.randint(0,100)

    for choice_player in range(6) :
        choice_player = int(input('Podaj liczbę: '))

        if choice_comp == choice_player:
            print('WYGRANA')
            break

        if 1 <= choice_comp - choice_player <= 15:
            print('GORĄCO')

        elif 16 <= choice_comp - choice_player <= 30:
            print('CIEPŁO')

        elif 31 <= choice_comp - choice_player <= 60:
            print('ZIMNO')

        else:
            print('LODOWATO')
    print('')
    print('.' * 9)
    print('PRZEGRANA')
    print('Liczba wylosowana przez przeciwnika:', choice_comp)
    revenge_1 = input('REWANŻ? WPISZ TAK/NIE: ')
