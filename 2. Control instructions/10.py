#Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
#Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5
while True:
    num = int(input('Podaj liczbę z zakresu 0 - 20: '))
    if num == secret_num:
        print('Udało Ci się zgadnąć cyfrę, gratulacje ! :)')
        break
    else:
        print('Spróbuj ponownie ;)')