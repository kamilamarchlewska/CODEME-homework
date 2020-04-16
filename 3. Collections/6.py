#Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie
# np. “Mój pies, rasy border collie wabi się Dyzio”.

tuple = ('kot', 'brytyjskiej', 'Pusia')

tuple_list = list(tuple)

print(f'Mój {tuple_list[0]}, rasy {tuple_list[1]}, wabi się {tuple_list[2]}. ')