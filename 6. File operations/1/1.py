#1▹ Utwórz plik na pulpicie zawierający listę ok. 10 cytatów.
#   Każdy cytat powinen się znaleźć w nowej linii.
#   Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś.
#   Zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
#   Plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora

#2▹ Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.

#3▹ Wyświetl tylko 5 pierwszych linii

#4▹ Wyświetl 3 losowe cytaty

import random
import os


def show_poem(text):
    poem = random.choice(text)
    poem = poem.split('.')
    print(poem[0].center(width))
    print(poem[1].center(width))


quotes_name = input('Podaj swoją nazwę pliku: ')
quotes_name = 'quotes_list.txt'


with open(quotes_name, 'r', encoding='utf-8') as quotes:
    poen = quotes.read().splitlines()

    width = 75
    print('CYTAT NA DZIŚ:'.center(width))
    print('*' * width)
    show_poem(poen)
    show_poem(poen)
    show_poem(poen)
    print('*' * width)

print('')
print('Rozmiar pliku to:', os.path.getsize('quotes_list.txt'), 'bajtów')