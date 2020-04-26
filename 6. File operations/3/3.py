#Wykorzystaj plik zawierający fragment Pana Tadeusza.
# Znajdź najdłuższe słowo występujące w zadanym fragmencie.


with open('pantadek.txt', encoding='utf-8') as poen:
    mr_tadeusz = poen.read()

mr_tadeusz = mr_tadeusz.replace(',', '')
mr_tadeusz = mr_tadeusz.replace('.', '')
mr_tadeusz = mr_tadeusz.replace(';', '')
mr_tadeusz = mr_tadeusz.replace(':', '')
mr_tadeusz = mr_tadeusz.split()


max_word = ''

for word in mr_tadeusz:
    if len(word) > len(max_word):
        max_word = word

print('Najdłuższe słowo to:', max_word)