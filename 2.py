#Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

numb_1 = int(input('Proszę o podanie pierwszej liczby: '))
numb_2 = int(input('Proszę o podanie drugiej cyfry: '))

amount = numb_1 + numb_2

if amount > 100:
    print('Suma tych liczb to:', amount)
else:
    print('Koniec')