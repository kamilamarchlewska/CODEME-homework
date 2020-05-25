class Student:
    university = 'Nicolaus Copernicus University'

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def email(self):
        return f'{self.name.lower()}.{self.surname.lower()}@gmail.com'

objectAnna = Student('Anna', 'Krajewska', '21')

print(objectAnna.surname)
print(objectAnna.email())
print(Student.email(objectAnna))