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

player_score = 0
comp_score = 0

print('Jeżeli będziesz chciał zakończyć grę wpisz "koniec."')
print('')
liczba = int(input('ILE RUND CHCESZ ROZEGRAĆ? '))

for player_selection in range(liczba) :
    player_selection = input('WYBIERZ FIGURĘ WPISUJĄC LICZBĘ: kamień (k) / papier (p) / nożyce (n): ')

    if player_selection == 'koniec':
        print('Dziękuję za grę :)')
        sys.exit(0)


    comp_selection = random.randint(1,3)

    if comp_selection == 1:
        comp_selection = 'k'
    elif comp_selection == 2:
        comp_selection = 'p'
    else:
        comp_selection = 'n'

    if player_selection == comp_selection:
        print('REMIS')

    elif player_selection == 'k' and comp_selection == 'p':
        print('KAMIEŃ VS PAPIER')
        print('PRZEGRANA')
        comp_score +=  1

    elif player_selection == 'k' and comp_selection == 'n':
        print('KAMIEŃ + NOŻYCE')
        print('WYGRANA')
        player_score += 1

    elif player_selection == 'p' and comp_selection == 'k':
        print('PAPIER VS KAMIEŃ')
        print('WYGRANA')
        player_score += 1

    elif player_selection == 'p' and comp_selection == 'n':
        print('PAPIER VS NOŻYCE')
        print('PRZEGRANA')
        comp_score +=  1

    elif player_selection == 'n' and comp_selection == 'k':
        print('NOŻYCE VS KAMIEŃ')
        print('PRZEGRANA')
        comp_score +=  1

    elif player_selection == 'n' and comp_selection == 'p':
        print('NOŻYCE VS PAPIER')
        print('WYGRANA')
        player_score += 1

    else:
        print('Nieprawidłowy parametr')

print('WYNIKI')
print('TWÓJ WYNIK:', player_score)
print('WYNIK PRZECIWNIKA', comp_score)

if player_score > comp_score:
    print('WYGRANA!')

elif player_score < comp_score:
    print('PRZEGRANA')
else:
    print('REMIS')

print('Dziękuję za grę :)')