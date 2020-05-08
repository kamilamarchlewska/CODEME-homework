#Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.

#Program zacznie ze stworzonym słownikiem o trzech kluczach:
#marka (str)
#model (str)
#rocznik (int)
#Wypisze ten słownik na ekran (bez żadnego formatowania)
#Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
#“Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#Jeśli nie spełnia powyższego warunku, wypisze komunikat:
#“Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.

import datetime

def carVintage():
    now = datetime.datetime.now()
    nowYear = str(now.year)
    nowYear = int(nowYear)
    carOld = nowYear - carAge
    if carOld >= 25:
        print(f'Gratulacje! Twój samochód {carBrand} może być zarejestrowany jako zabytek.')
    else:
        print(f'Twój samochód {carBrand} jest jeszcze zbyt młody.')


carDict = {'marka':'MBW', 'model':'E33', 'rocznik':'1992'}

print('DANE AUTA:')
for key,value in carDict.items():
    print('◄', key, value)

carValue = carDict.values()
carList = list(carValue)
carAge = int(carList[2])

carBrand = carDict['marka']

carVintage()