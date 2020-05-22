# Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index.
# Podziel 1 przez liczbę pod indexem wybranym przez użytkownika.
# Obsłuż błędy.

myList = [1, 'a', 3, 'b', 'c', 'd', '>', 8, ' ', ' 1, 2, 3, 4,']

try:
    giveIndex = int(input('Give index to the list: '))
    division = myList[giveIndex] / 1
    print(division)

except TypeError:
    print('TypeError')

except  ValueError:
    print('ValueError')

else:
    print('Coala Bears')