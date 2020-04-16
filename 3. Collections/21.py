#Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
#Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.

dict_UK = {}.fromkeys(['Meaghan', 'Dior', 'Adalee', 'Palmer', 'Oaklynn', 'Haisley', 'Keily', 'Novah', 'Yara', 'Ensley'], 'UK')
dict_Canada = {}.fromkeys(['Abigail', 'Leah', 'Hazel', 'Violet', 'Aurora', 'Avery', 'Sofia', 'Camila', 'Aria', 'Scarlett'], 'Canada')
dict_Australia = {}.fromkeys(['Victoria', 'Madison', 'Luna', 'Grace', 'Leah', 'Hazel', 'Violet', 'Aurora', 'Zoey', 'Nora'], 'Australia')
dict_New_Zealand = {}.fromkeys(['Lily', 'Eleanor', 'Hannah', 'Lillian', 'Addison', 'Aubrey', 'Ellie', 'Stella', 'Natalie', 'Zoe'], 'New Zealand')
dict_France = {}.fromkeys(['Leah', 'Hazel', 'Violet', 'Aurora', 'Savannah', 'Audrey', 'Brooklyn', 'Bella', 'Claire', 'Skylar'], 'France')
dict_Spain = {}.fromkeys(['Lucy', 'Paisley', 'Everly', 'Anna', 'Caroline', 'Nova Genesis', 'Emilia', 'Kennedy', 'Samantha'], 'Spain')
dict_Iceland = {}.fromkeys(['Maya', 'Willow', 'Kinsley', 'Naomi', 'Aaliyah', 'Elena', 'Sarah', 'Ariana', 'Allison', 'Gabriella'], 'Iceland')
dict_Israel = {}.fromkeys(['Alice', 'Madelyn', 'Cora', 'Ruby', 'Eva', 'Serenity', 'Autumn', 'Adeline', 'Hailey', 'Gianna'], 'Israel')
dict_Mexico = {}.fromkeys(['Sofia', 'Isla', 'Eliana', 'Quinn', 'Nevaeh', 'Ivy', 'Sadie', 'Piper', 'Lydia', 'Alexa'], 'Mexico')
dict_Russia = {}.fromkeys(['Svetlana', 'Emery', 'Julia', 'Olga', 'Arianna', 'Sofia', 'Irina', 'Tatiana', 'Brielle', 'Daria'], 'Russia')


list_UK = list(dict_UK)
list_Canada = list(dict_Canada)
list_Australia = list(dict_Australia)
list_New_Zealand = list(dict_New_Zealand)
list_France = list(dict_France)
list_Spain = list(dict_Spain)
list_Iceland = list(dict_Iceland)
list_Israel = list(dict_Israel)
list_Mexico = list(dict_Mexico)
list_Russia = list(dict_Russia)

lista = list_UK + list_Canada + list_Australia + list_New_Zealand + list_France + list_Spain + list_Iceland + list_Israel + list_Mexico + list_Russia

#Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

listas = []
for k in lista:
    coun = lista.count(k)
    if coun >= 3:
        listas.append(k)

for m in listas:
    listas.remove(m)

print(listas)

