#Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.
width = 50
print('-' * width)
for k in range(1,11):
    for m in range(1,11):
        print(f'{k * m:^4}', end='|')
    print()
    print('-' * width)
