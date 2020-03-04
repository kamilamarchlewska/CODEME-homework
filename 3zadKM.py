# Zadanie 3

print("------------------ Sumowanie liczb ------------------")
#print("Program pyta użytkownika o 4 dowolne liczby całkowite")
#print("a następnie zwraca ich sumę.")
#print()

a, b, c, d = input("Podaj cztery liczby całkowite oddzielone spacjami: ").split(" ") 
print("Wprowadzono liczby:", a, b, c, d)

first_number = int(a) #przechowuje jedną wartość
second_number = int(b)
third_number = int(c)
fourth_number = int(d)

total = first_number + second_number + third_number + fourth_number

print('Suma podanych cyfr wynosi:', total)
