#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

word = 'Abracadabra'
#1. Sprawdzam który numer ma środkowy znak
middle = len(word)//2
#2. Wyciągam 4 i 7 ( 3 środkowe litery)
a = word[4:middle]
b = word[middle:7]
print(a)
print(b)

print(a + b)