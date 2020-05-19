import formula_delta

def deltaHeader():
    header = 'DELTA CALCULATOR'
    width = len(header)

    print('-' * width)
    print(header)
    print('-' * width)
    print()


deltaHeader()

a = int(input('Enter "a" value:'))
b = int(input('Enter "b" value:'))
c = int(input('Enter "c" value:'))

formula_delta.delta(a, b, c)
