#Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5
zmienna = 0

while zmienna != secret_num:
    zmienna = int(input('Proszę o podanie cyfry od 0 do 20: '))
    if zmienna == secret_num:
        print('Udało się! Ta cyfra to', secret_num, '.')
    else:
        if zmienna < 5:
            print('Cyfra jest większa ')
        else:
            print('Cyfra jest mniejsza ')