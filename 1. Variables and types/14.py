# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

a, b, c = input("Podaj trzy liczby całkowite oddzielone spacjami: ").split(" ")
print("Dziękuję :) Wprowadzone liczby to:", a, b, c)

first_number = int(a) #przechowuje jedną wartość
second_number = int(b)
third_number = int(c)

print('Python potrafi wykonywać obliczenia')

print('Najpierw pomnoży dla Ciebie 2 pierwsze liczby...')
multiplication = first_number * second_number
print('Wynik mnożenia to', multiplication)

print('A na koniec podzieli przez ostatnią cyfrę')
division = multiplication / third_number

print('Otrzymujesz wynik', round(division, 2))
print('Zobacz jaki ten pytonek fajny :)')