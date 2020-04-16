#Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

tuple = (1, 2, 3, 4, 2, 3, 1, 12)

a = tuple.count(1)
b = tuple.count(2)
c = tuple.count(3)
d = tuple.count(4)
e = tuple.count(12)

tuple_2 = list(tuple)
repeating_list = []

if a > 1:
    repeating_list.append(tuple_2[0])
if b > 1:
    repeating_list.append(tuple_2[1])
if c > 1:
    repeating_list.append(tuple_2[2])
if d > 1:
    repeating_list.append(tuple_2[3])
if e > 1:
    repeating_list.append(tuple_2[8])

print('Powtarzające się cyfry to:', repeating_list)