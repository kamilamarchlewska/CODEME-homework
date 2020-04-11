# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

print('Ocena książki "W pustyni i w puszczy " Henryka Sienkiewicza.')
print('Proszę o podanie oceny od 0-10 w zależności od podanej kategori.')
opinion_first = int(input('Główni bohaterowie: '))
opinion_second = int(input('Opisy przyrody: '))
opinion_third = int(input('Fabuła: '))

evaluation = (opinion_first + opinion_second + opinion_third) // 3

if evaluation <= 4:
    print('Ocena - książka nie warta uwagi.')

elif 5 >= evaluation <= 7:
    print('Ocena - przeciętna ksiązka.')

else:
    print('Ocena: Książka jest bardzo dobra.')