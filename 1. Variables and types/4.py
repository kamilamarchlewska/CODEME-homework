#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.


combustion = float(input('Proszę o podanie wartości spalania na 100 km w l: '))
route = float(input('Proszę o podanie długości trasy w km: '))
cost = float(input('Podaj cenę benzyny: '))

expedition_cost = (((route / 100) * combustion) * cost)
print('Koszt wyprawy to:', round(expedition_cost, 2), 'PLN')