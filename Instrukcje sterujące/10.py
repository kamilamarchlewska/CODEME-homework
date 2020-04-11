#Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

#C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

#Napisz rozwiązanie zarówno z użyciem pętli while jak i for.
print('.' * 84)

for c in range(0, 200, 20):
    cz = 5 / 9 * (c - 31)
    print('Temperatura w stopniach Fahrenheit:', c, "|", 'Temperatura w stopniach Celcjusza:', round(cz, 2))

fahr = 0

print('.' * 84)

while fahr <= 200:
    cel = C = 5/9 * (fahr - 32)
    print('Temperatura w stopniach Fahrenheit:', fahr, "|", 'Temperatura w stopniach Celcjusza:', round(cel, 2))
    fahr = fahr + 20