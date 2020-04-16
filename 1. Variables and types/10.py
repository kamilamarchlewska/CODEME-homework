#Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
print('Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej. ')
print('............. Czy podane przez Ciebie zdanie jest Palindromem? Sprawdź :) ...............')
print()
palindrom_please = input('Proszę o podanie zdania: ')
palindrom_please = palindrom_please.lower()
palindrom_please = palindrom_please.replace(' ', '')

if palindrom_please is palindrom_please[::-1]:
    print('Podane zdanie jest Palindromem')

else:
    print('Podane zdanie nie jest Palindromem.')
    print('Przykład zdania które jest Palindromem: Kobyła ma mały bok. ')