# Oblicz średnią arymetyczną z kilku liczb.
# Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinen być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

def arithmeticAverage(a, b, c, d):
    sumNumbers = 0
    for Numb in listNumbers:
        sumNumbers = sumNumbers + int(Numb)

    average = sumNumbers / 4
    print(average)

try:
    a, b, c, d = input("Provide four integers (numbers split by commas): ").split(",")
    listNumbers = [a, b, c, d]

    arithmeticAverage(a, b, c, d)
except ValueError:
    print('Ups... you see error report.')
    filename = ('error report.txt')
    with open (filename, 'w+') as error:
        error.write('ValueError')
else:
    print('koala bear')