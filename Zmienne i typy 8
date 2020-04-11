# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.

print('KANTOR ONLINE - NISKIE CENY')

exchange_euro = 4.19
exchange_dolar = 3.90

a = input("Proszę o podanie kwoty która zostanie wykorzystana w docelowym miejscu: ")
print("Dziękuję. Wprowadzona kwota wynosi:", a, 'PLN')

money_holiday = float(a)

currency_what = input('Z jakiej waluty skorzystasz w docelowym miejscu? WPISZ EURO LUB DOLAR: ')
if currency_what != 'DOLAR':
    calculation_euro = money_holiday / exchange_euro
    print('Kwota po przeliczeniu wynosi', round(calculation_euro), '€')
    l = input('Proszę o podanie nominału w jakim ma zostać wypłacona kwota. Dostępne nominały: 50, 20, 10, 5: ' )
    if l == '10':
        euros = calculation_euro / 10
        print('Ilość banknotów którą otrzymasz to:', round(euros))
    if l == '5':
        euroxs = calculation_euro / 5
        print('Ilość banknotów którą otrzymasz to:', round(euroxs))
    if l == '20':
        eurom = calculation_euro / 20
        print('Ilość banknotów którą otrzymasz to:', round(eurom))
    if l == "50":
        eurol = calculation_euro / 50
        print('Ilość banknotów którą otrzymasz to:', round(eurol))
else:
    calculation_dolary = money_holiday / exchange_dolar
    print('Kwota po przeliczeniu wynosi', round(calculation_dolary), '$')
    l = input('Proszę o podanie nominału w jakim ma zostać wypłacona kwota. Dostępne nominały: 50, 20, 10, 5: ' )
    if l == '10':
        dolars = calculation_dolary / 10
        print('Ilość banknotów którą otrzymasz to:', round(dolars))
    if l == '5':
        dolarxs = calculation_dolary / 5
        print('Ilość banknotów którą otrzymasz to:', round(dolarxs))
    if l == '50':
        dolarm = calculation_dolary / 50
        print('Ilość banknotów którą otrzymasz to:', round(dolarm))
    if l =="20":
        dolarl = calculation_dolary / 20
        print('Ilość banknotów którą otrzymasz to:', round(dolarl))

print('Życzymy miłej podróży')
