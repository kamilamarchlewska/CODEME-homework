# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia.

a, b = input("Podaj dwie liczby całkowite oddzielone spacjami: ").split(" ")
print("Dziękuję :) Wprowadzone liczby to:", a, b)

first_number = int(a)
second_number = int(b)

division = first_number / second_number
print('Wynik dzielenia to:', round(division, 2))

idivision = int(division)

if idivision < 1:
    print('Pierwsza liczba zmieści się w drugiej tylko raz')
else:
    print('Pierwsza liczba zmieści się w drugiej wielokrotnie')
    print('Dokładnie' , round(division), 'razy')

reszta_dzielenia = first_number % second_number
print('A reszta dzielenia wynosi:', reszta_dzielenia)