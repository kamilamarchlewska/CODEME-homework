# Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku z cytatami.
# Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.

import random
import os


def show_poem(text):
    poem = random.choice(text)
    poem = poem.split('.')
    width = 75
    print(poem[0].center(width))
    print(poem[1].center(width))

def poen(quotes_name):

    with open(quotes_name, 'r', encoding='utf-8') as quotes:
        poen = quotes.read().splitlines()

    width = 75
    print('CYTAT NA DZIŚ:'.center(width))
    print('*' * width)
    show_poem(poen)
    print('*' * width)

try:
    quotes_name = input('Podaj nazwę pliku: ')
    poen(quotes_name)

except FileNotFoundError:
    print('Podano nieprawidłową nazwę pliku')
    quotes_name = input('Podaj prawidłową nazwę pliku: ')
    poen(quotes_name)

except PermissionError:
    print('Podano nieprawidłową nazwę pliku')
    quotes_name = input('Podaj prawidłową nazwę pliku: ')
    poen(quotes_name)
else:
    print('Dane są nieprawidłowe')