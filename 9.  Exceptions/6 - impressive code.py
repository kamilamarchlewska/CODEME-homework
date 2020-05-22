#Wybierz zadanie z wszystkich zadań kursowych, które wg Ciebie jest twoim najbardziej imponującym kodem napisanym do tej pory.
# Popraw ten kod zgodnie z tym czego się do tej pory nauczyłeś.

import sys

def header(): #address book header
    # formatting - centering the text
    print('-' * 52)
    print('{:^52s}'.format('ADDRESS BOOK - CONTACT NUMBERS'))
    print('-' * 52)
    print('{:^52s}'.format('MENU'))
    print('{:^52s}'.format('VIEW ALL CONTACTS | ENTER : ALL'))
    print('{:^52s}'.format('CREATE A NEW CONTACT | ENTER: NEW'))
    print('{:^52s}'.format('DELETE CONTACT | ENTER: DELETE'))
    print('{:^52s}'.format('EXIT THE PROGRAM | ENTER: EXIT'))
    print('-' * 52)
    print()


def koniec(selection_user):  # - End of program work
    if selection_user == 'exit':
        print('THANK YOU FOR USING THIS PROGRAM')


def delete(selection_user):  # - Delete contact
    if selection_user == "delete":
        try:
            entry = input('How to delete contact (give the name)? : ')
            entry_1 = entry.upper()
            friends_data.pop(entry_1)
        except KeyError:
            print('Invalid contact provided. Try again.')
            entry = input('How to delete contact (give the name)? : ')
            entry_1 = entry.upper()
            friends_data.pop(entry_1)


def new(selection_user):  # - Create a new contact
    if selection_user == 'new':
        name = input('Provide contact name: ')
        number = input('Provide contact number: ')
        name = name.upper()
        friends_data[name] = number


def all(selection_user):  # - Display all contacts
    if selection_user == 'all':
        print(friends_data)


header() #address book header

# - Wprowadzone kilka wpisów
friends_data = {'ANNA': '733270764', 'IWONA': '633258974', 'STASIEK': '477877985'}
print(f'ADDRESS BOOK: {friends_data}')

# endless loop - end of sys.exit(0)
while True:
    selection_user = input('What action do you want to perform? ')
    selection_user = selection_user.lower()
    koniec(selection_user)
    delete(selection_user)
    new(selection_user)
    all(selection_user)