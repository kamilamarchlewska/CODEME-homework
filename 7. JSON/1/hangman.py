#Popraw kod wisielca, tak by pobierać hasła do gry z pliku hangman.json.
# Plik powinnien zawierać conamniej jedno zagnieżdżenie odpowiadające kategoriom, które użytkownik może wybrać w grze.
# Kategorie pobrane z pliku JSON pojawiają się jako elementy menu start.



import json
import random



def hangman(text):
    secret = text

    characters = list(secret)
    for i in range(len(secret)):
        characters[i] = '_'

    life = len(secret) + 2
    print(f'Masz {life} prób :)')
    print('')

    while life > 0:
        print(f'Pozostało ci {life} prób.')
        print(' '.join(characters))

        letter = input('Proszę o podanie litery:')
        if letter in secret:
            for i in range(len(secret)):
                if secret[i] == letter:
                    characters[i] = letter
                    life -= 1
                    a = characters.count('_')
                    if a == 0:
                        print(f'Hasło to: {secret}. ')
                        print('Wygrana!')
                        life -= 20

                    if characters[i] == secret:
                        print('Wygrana!')

                    if characters[i] == secret:
                        print('Wygrana!')
                        break



            if letter == secret:
                print('Wygrana!')
                break

        else:
            life -= 1

    if life == 0:
        print('Przegrana!')
        print(f'Hasło to: {secret}. ')

def choice_category():
    if category == 1:
        flower_choice = random.choice(data['1. KWIATY'])
        hangman(flower_choice)


    elif category == 2:
        fruit_choice = random.choice(data['2. OWOCE'])
        hangman(fruit_choice)


    elif category == 3:
        vegetable_choice = random.choice(data['3. WARZYWA'])
        hangman(vegetable_choice)


    elif category == 4:
        animal_choice = random.choice(data['4. ZWIERZETA'])
        hangman(animal_choice)

    else:
        print('Zły wybór')

def header_hangman():
    width = 24
    print('|  DOSTĘPNE KATEGORIE: |')
    print('.' * width)
    for i in dict_categories:
        print(i.center(width))

    print('.' * width)
    print('')


filename = 'hangman.json'
with open(filename, 'r') as f:
  data = json.loads(f.read())

dict_categories = data.keys()

header_hangman()
category = int(input('Proszę o podanie numeru kategorii: '))
choice_category()
