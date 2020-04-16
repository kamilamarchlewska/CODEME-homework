#Utwórz 2 krotki.
# Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple_2 = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

result = list(tuple_1[::2] + tuple_2[1::2])
result = set(result)

print(result)