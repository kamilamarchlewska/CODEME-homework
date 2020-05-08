import datetime
import json



def carVintage():
    now = datetime.datetime.now()
    nowYear = str(now.year)
    nowYear = int(nowYear)
    carOld = nowYear - carAge
    if carOld >= 25:
        print(f'Gratulacje! Twój samochód {carBrand} może być zarejestrowany jako zabytek.')
    else:
        print(f'Twój samochód {carBrand} jest jeszcze zbyt młody.')


filename = 'infoCarVintage'
with open(filename, 'r') as Info:
  carDict = json.loads(Info.read())


print('DANE AUTA:')
for key,value in carDict.items():
    print('◄', key, value)

carValue = carDict.values()
carList = list(carValue)
carAge = int(carList[2])

carBrand = carDict['marka']

carVintage()