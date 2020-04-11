#Napisz grę - kamień (k) / papier (p) / nożyce (n).
#Użytkownik podaje jedną z 3 figur.
#Komputer losuje jedną z 3 figur.
#Sprawdź kto wygrał tę rundę.
#Zmień kod tak, by użytkownik mógł podac liczbę rund.
#Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random
import sys


print('GRA KAMIEŃ PAPIER NOŻYCE')

wynik_gracz = 0
wynik_komp = 0

print('Jeżeli będziesz chciał zakończyć grę wpisz "koniec."')
print('')
liczba = int(input('ILE RUND CHCESZ ROZEGRAĆ? '))

for wybor_gracz in range(liczba) :
    wybor_gracz = input('WYBIERZ FIGURĘ WPISUJĄC LICZBĘ: kamień (k) / papier (p) / nożyce (n): ')

    if wybor_gracz == 'koniec':
        print('Dziękuję za grę :)')
        sys.exit(0)


    wybor_komp = random.randint(1,3)

    if wybor_komp == 1:
        wybor_komp = 'k'
    elif wybor_komp == 2:
        wybor_komp = 'p'
    else:
        wybor_komp = 'n'

    if wybor_gracz == wynik_komp:
        print('REMIS')

    elif wybor_gracz == 'k' and wybor_komp == 'p':
        print('KAMIEŃ VS PAPIER')
        print('PRZEGRANA')
        wynik_komp +=  1

    elif wybor_gracz == 'k' and wybor_komp == 'n':
        print('KAMIEŃ + NOŻYCE')
        print('WYGRANA')
        wynik_gracz += 1

    elif wybor_gracz == 'p' and wybor_komp == 'k':
        print('PAPIER VS KAMIEŃ')
        print('WYGRANA')
        wynik_gracz += 1

    elif wybor_gracz == 'p' and wybor_komp == 'n':
        print('PAPIER VS NOŻYCE')
        print('PRZEGRANA')
        wynik_komp +=  1

    elif wybor_gracz == 'n' and wybor_komp == 'k':
        print('NOŻYCE VS KAMIEŃ')
        print('PRZEGRANA')
        wynik_komp +=  1

    elif wybor_gracz == 'n' and wybor_komp == 'p':
        print('NOŻYCE VS PAPIER')
        print('WYGRANA')
        wynik_gracz += 1

    else:
        print('Nieprawidłowy parametr')

print('WYNIKI')
print('TWÓJ WYNIK:', wynik_gracz)
print('WYNIK PRZECIWNIKA', wynik_komp)

if wynik_gracz > wynik_komp:
    print('WYGRANA!')

elif wynik_gracz < wynik_komp:
    print('PRZEGRANA')
else:
    print('REMIS')

print('Dziękuję za grę :)')