# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość.
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy (jest to prawdopodobne)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

print('Hej ;) Dziś sprawdzimy ile miejsca pozostanie w windzie gdy wstawimy do niej lodówkę')
print('Zmierzyłam lodówkę i okazało się że jej wymiary to 2m x 1.5m x 1.1m. Spora bestia.')

height = 2
width = 1.5
depth = 1.1

volume_fridge = height * width * depth
print('Wyliczyłam że jej objętość wynosi', round(volume_fridge, 2) , "m3", "Dobrze...")
print('Znalazłam nazwę windy, zapytałam wujka google jaką ma objętość i otrzymałam informację - 10.2 m3')

volume_elevator = 10.2
space_free = volume_elevator - volume_fridge

print('Wow! Zostało nam ', round(space_free, 2),"m3", '.', 'Możemy jeszcze wpakować szafę! :)')
