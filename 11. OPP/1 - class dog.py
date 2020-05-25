#Create a dog class - the class has attributes and a method.
#attributes: name, coat color, breed
#methods - bark, tail wag
#Create several dog objects with different parameters

class Dog:

    def __init__(self, name, coatColor, breed):
        self.name = name
        self.coatColor = coatColor
        self.breed = breed

    def barkingDog(self):
        return f'{self.name} hau hau!'

    def wagTail(self):
        return f'{self.name} wags its tail.'

objectDyzio = Dog('Dyzio', 'black', 'Maltese ')
objectDaisy = Dog('Daisy', 'White', 'Mountain')
objectNemo = Dog('Nemo', 'Brown', 'Husky')

print(f'Name - {objectDyzio.name} | Coat Color - {objectDyzio.coatColor} | Breed - {objectDyzio.breed}')
print(f'Name - {objectDaisy.name} | Coat Color - {objectDaisy.coatColor} | Breed - {objectDaisy.breed}')
print(f'Name - {objectNemo.name}  | Coat Color - {objectNemo.coatColor} | Breed - {objectNemo.breed}')
print(objectDaisy.barkingDog())
print(objectNemo.wagTail())