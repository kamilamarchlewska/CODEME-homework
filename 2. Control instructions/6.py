#Sortowanie.
# Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

a = input('Proszę o podanie 1 liczby:')
b = input('Prosze o podanie 2 liczby:')
c = input('Proszę o podanie 3 liczby:')

d = sorted([a, b, c])
print('Podane liczby to:', d)

print(max(a, b, c), 'to największa cyfra.')

