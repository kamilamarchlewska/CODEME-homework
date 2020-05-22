#Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie.
# Obsłuż błąd

myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

try:
    giveIndex = int(input('Give index to the tuple: '))
    giveValue = input('Give value to the tuple: ')

    myTuple[giveIndex] = giveValue
    print(myTuple[giveIndex])

except TypeError:
    print('TypeError')

except ValueError:
    print('ValueError')

else:
    print('koala bears')