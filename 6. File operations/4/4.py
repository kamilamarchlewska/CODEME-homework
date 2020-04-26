# Wisielec.
# Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc.
# Poproś użytkownika o podanie kategorii przed rozpoczęciemy gry.
# Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
# Rozgrywka powinna być maksymalnie intuicyjna.

import random

def hangman(text):
    secret = text

    characters = list(secret)
    for i in range(len(secret)):
        characters[i] = '_'

    life = len(secret) + 2
    print(f'Masz {life} prób')

    while life > 0:
        print(f'Pozostało ci {life} prób')
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

width = 23

print('| DOSTĘPNE KATEGORIE: |')
print('.' * width)
print('1. KWIATY'.center(23))
print('2. OWOCE'.center(23))
print('3. WARZYWA'.center(23))
print('4. ZWIERZĘTA'.center(23))
print('.' * width)

category = int(input('Proszę o podanie numeru kategorii: '))

if category == 1:
    with open('flowers.txt') as flowers:
        flower = flowers.read()
        flower = flower.split()
        flower_choice = random.choice(flower)
        hangman(flower_choice)


elif category == 2:
    with open('fruits.txt') as fruits:
        fruit = fruits.read()
        fruit = fruit.split()
        fruit_choice = random.choice(fruit)
        hangman(fruit_choice)


elif category == 3:
    with open('vegetables.txt') as vegetables:
        vegetable = vegetables.read()
        vegetable = vegetable.split()
        vegetable_choice = random.choice(vegetable)
        hangman(vegetable_choice)


elif category == 4:
    with open('animals.txt') as animals:
        animal = animals.read()
        animal = animal.split()
        animal_choice = random.choice(animal)
        hangman(animal_choice)

else:
    print('Zły wybór')