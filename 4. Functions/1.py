#Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

def radiuss():
    radius = int(input('Proszę o podanie promienia pola: '))
    p = 4.13 * (radius ** 2)
    print(f'Pole koła na podstawie promienia {radius} to {p} cm2')
    return


radiuss()