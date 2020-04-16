#Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

title = input('Proszę o podanie tytułu książki: ')
surname = input('Proszę o podanie nazwiska autora: ')
pages_num = input('Proszę o podanie liczby stron: ')

#Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
if title.isalpha() is True:
    print('Tytuł składa się z samych liter.')
else:
    print('Tytuł nie składa się z samych liter.')

if surname.isalpha() is True:
    print('Nazwisko składa się z samych liter.')
else:
    print('Nazwisko nie składa się z samych liter.')

if pages_num.isdigit() is True:
    print('Liczba stron składa się z samych cyfr.')
else:
    print('Liczba stron składa się z samych cyfr.')
#Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
title_big = title.capitalize()
surname_big = surname.capitalize()
#Połącz dane w jeden ciąg book za pomocą spacji
list1 = [title_big, surname_big, pages_num]
print(' '.join(list1))

#Policz liczbę wszystkich znaków w napisie book
a = 'book'
b = len(a)
print('Liczba wszystkich znaków w napisie', a, 'to', b)
