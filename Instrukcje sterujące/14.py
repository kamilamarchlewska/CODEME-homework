#Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

print('Pierwszy szablon powitania:')
list = []
name = input('Proszę o podanie imion oddzielonych spacją: ')

list.append(name)

print('Osoby na liście to:', list, 'Witam!')

print(' ')
print('Drugi szablon powitania:')

names = input('Proszę o podanie imion oddzielonych spacją: ')

names = names.split(' ')
print('Osoby na liście to:', names)

powitanie = (' miło Cię poznać!')

for person in names:
    print(person + powitanie)