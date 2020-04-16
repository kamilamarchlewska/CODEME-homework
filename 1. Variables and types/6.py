#Do zmiennej quote przypisz zdanie:
quote = '„Honesty is the first chapter in the book of wisdom.”'
#„Honesty is the first chapter in the book of wisdom.”, a następnie:

#Policz wszystkie znaki w napisie
print(len(quote))
#Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-8:-2])
#Wyświetl tylko pierwszą połowę tekstu
middle = len(quote)//2
print(quote[0:middle])
#Wyświetl tylko kropkę
print(quote[-2])
#Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[middle::3])
#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])
#Wyświetl cały cytat odwrotnie
print(quote[::-1])
#Zamień wisdom na słowo friendship
print(quote.replace('wisdom', 'friendship'))