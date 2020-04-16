#Stwórz krotkę liczb całkowitych.
# Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.

tuple = (1, 2, 3, 4, 5, 6, 7)

l = int(input('Podaj cyfrę: '))

if l in tuple:
    print('Indeks cyfry to:', tuple.index(l))