#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = ('HokusPokus')
s2 = (' Tygrys ')
print('Podstawowe zaklęcie to:', s1)

a = len(s1)//2

part_first = s1[:a]
part_second = s1[a:]

magic = part_first + s2 + part_second
print('A kiedy chcesz przywołać tygrysa wypowiadasz słowa:', magic)