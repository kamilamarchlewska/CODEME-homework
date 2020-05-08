# Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
# W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
# ponownie wyświetl zmieniony słownik
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności.
# Dopisz odpowiednie komunikaty.

import datetime

def carVintage():
    now = datetime.datetime.now()
    nowYear = str(now.year)
    nowYear = int(nowYear)
    carOld = nowYear - carAge


    if carOld >= 25 and carParts == 'TAK':
        print(f'Gratulacje! Twój samochód {carBrand} może być zarejestrowany jako zabytek.')

    elif carOld >= 25 and carParts == 'NIE':
        print(f'Twój samochód {carBrand} nie może być zarejestrowany jako zabytek.')
        print(f'{carBrand} ma mniej niż 75% oryginalnych części.')
        print('Spełnia kryterium dotyczące wieku auta.')

    elif carOld < 25 and carParts == 'TAK':
        print(f'Twój samochód {carBrand} nie może być zarejestrowany jako zabytek.')
        print(f'{carBrand} posiada co najmniej 75% oryginalnych części.')
        print('Nie spełnia kryterium dotyczące wieku auta.')
    else:
        print(f'Twój samochód {carBrand} jest jeszcze zbyt młody.')


carDict = {'marka':'MBW', 'model':'E33', 'rocznik':'1992', 'czy oryginalny?':'NIE'}

print('DANE AUTA:')
for key,value in carDict.items():
    print('◄', key, value)

carValue = carDict.values()
carList = list(carValue)
carAge = int(carList[2])

carBrand = carDict['marka']
carParts = carDict['czy oryginalny?']
carVintage()