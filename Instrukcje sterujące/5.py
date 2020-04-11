#Stwórz zmienną password.
#Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
#Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
#Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input('Proszę o podanie hasła:')

password_y = password.isalnum()
if password_y is True:
    print('Hasło składa się z liter i cyfr.')
else:
    print('Hasło powinno składać z liter i cyfr.')

password_l = password.islower()
if password_l is True:
    print('Hasło nie zawiera conajmniej 1 dużej litery.')
else:
    print('Hasło ma conajmniej 1 dużą literę.')

password_num = len(password)
if password_num >= 8:
    print('Hasło ma prawidłową długość.')
else:
    print('Hasło powinno mieć długość conajmniej 8 znaków.')