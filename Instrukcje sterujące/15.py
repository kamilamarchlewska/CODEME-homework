#Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

magic = input('Proszę o podanie zaklęcia: ')

magic = magic.replace(' ', '')

print(magic[1::2])

