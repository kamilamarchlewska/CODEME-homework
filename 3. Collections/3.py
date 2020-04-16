#Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

list = []

for k in range(5):
    k = int(input('Podaj cyfrę: '))
    list.append(k)

print('Podane cyfry to:', list)

if list[0] == list[-1]:
    print('pierwszy i ostatni element są takie same ;)')