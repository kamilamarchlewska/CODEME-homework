#Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def return_1():
    list = []
    for i in range(10):
        i = int(input('Proszę o podanie cyfry: '))
        list.append(i)
    print(f'Prodane liczby to: {list}.')

    sum_numbers = sum(list)
    print(sum_numbers)


return_1()

