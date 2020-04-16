#Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

example_list_2 = example_list.copy()
example_list_2 = tuple(example_list_2)

a = min(example_list_2)
b = max(example_list_2)

print(a)
print(b)
