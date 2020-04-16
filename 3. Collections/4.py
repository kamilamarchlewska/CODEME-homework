#Pobierz od użytkownika parzystą listę elementów.
# Sprawdź czy 2 środkowe elementy są takie same.

list = []


for k in range(6):
    k = int(input('Podaj cyfrę:'))
    list.append(k)

print('Podane liczby to: ', list)
if list[2] == list[-3]:
    print('2 środkowe elementy są takie same ;)')