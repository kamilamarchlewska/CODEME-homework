#Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#Dorota, Wellman, dziennikarka
#Adam, Małysz, sportowiec
#Robert, Lewandowski, piłkarz
#Krystyna, Janda, aktorka

list = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]

szer = 63
print('-' * szer)
print(f'|IMIĘ: {list[0][0]}  |', f'|NAZWISKO: {list[0][1]}    |', f'|ZAWÓD : {list[0][2]}|')
print(f'|IMIĘ: {list[1][0]}    |', f'|NAZWISKO: {list[1][1]}     |', f'|ZAWÓD : {list[1][2]}  |')
print(f'|IMIĘ: {list[2][0]}  |', f'|NAZWISKO: {list[2][1]}|', f'|ZAWÓD : {list[2][2]}     |')
print(f'|IMIĘ: {list[3][0]}|', f'|NAZWISKO: {list[3][1]}      |', f'|ZAWÓD : {list[3][2]}     |')
print('-' * szer)
