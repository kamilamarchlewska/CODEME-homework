#Stwórz grę ciepło zimno.
#Komputer losuje liczbę z zakresu od 1 do 100.
#Użytkownik podaje swój traf.
#Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#Jeśli użytkownik zgadnie wygrywa gracz.
#Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

print('GRA CIEPŁO ZIMNO')
pomoc = input('CZY CHCESZ ZAPOZNAĆ SIĘ Z ZASADAMI GRY? WPISZ TAK/NIE: ')

if pomoc == 'TAK':
    print('''1. Przeciwnik losuje liczbę z zakresu od 1 do 100.
    2. Podajesz swój traf od 1 do 100. Masz 6 prób do wykorzystania.
    3. Przeciwnik odpowiada ciepło zimno.
    4. Jeżeli w ciągu 6 prób - wygrywasz :)
    5. Jeżeli nie uda Ci się zgadnąć - wygrywa przeciwnik.
    
ZACZYNAMY! ''')

else:
    print('')
    print('ZACZYNAMY!')

rewanz = 'TAK'
while rewanz == 'TAK':

    wybor_komputer = random.randint(0,100)

    for wybor_gracz in range(6) :
        wybor_gracz = int(input('Podaj liczbę: '))

        if wybor_komputer == wybor_gracz:
            print('WYGRANA')
            break

        if 1 <= wybor_komputer - wybor_gracz <= 15:
            print('GORĄCO')

        elif 16 <= wybor_komputer - wybor_gracz <= 30:
            print('CIEPŁO')

        elif 31 <= wybor_komputer - wybor_gracz <= 60:
            print('ZIMNO')

        else:
            print('LODOWATO')
    print('')
    print('.' * 9)
    print('PRZEGRANA')
    print('Liczba wylosowana przez przeciwnika:', wybor_komputer)
    rewanzt = input('REWANŻ? WPISZ TAK/NIE: ')
