#Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.
#Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)


def return_1():
    list = []
    list_even = []
    for i in range(10):
        i = int(input('Proszę o podanie cyfry: '))
        list.append(i)
        p = i % 2
        if p == 0:
            list_even.append(i)

    print(f'Prodane liczby to: {list}.')
    print(f'Parzyste liczby to {list_even}')


return_1()

