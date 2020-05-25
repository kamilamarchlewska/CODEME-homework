# Create a class for orchids.
# Orchids have different colors, names etc.
# Create any attributes and methods.
# Add a common attribute - plant kingdom.

class Orchids:

    kindom = 'Kingdom of plants'

    def __init__(self, name, tribe, color):
        self.name = name
        self.tribe = tribe
        self.color = color

    def wateringDirectly(self):
        return 'Pour water into the pot. Don\'t wet the leaves!'

    def wateringUnder(self):
        return 'Put the pot into the water. Hold the pot in water for 15 minutes.'

orchid_1 = Orchids('Rhynchostele rossii', 'Cymbidieae', 'white - brown with spots')
orchid_2 = Orchids('Dendrobium leonis', 'Dendrobieae', 'yellow')
orchid_3 = Orchids('Fernandezia maculata', 'Cymbidieae', 'fiery red')

print('***** LIST OF ORCHIDS *****')

print(f'| Name - {orchid_1.name} | Tribe - {orchid_1.tribe} | Cor - {orchid_1.color} |')
print(f'| Orchid watering - {orchid_1.wateringDirectly()}')
print('')
print(f'| Name - {orchid_2.name} | Tribe - {orchid_2.tribe} | Cor - {orchid_2.color} |')
print(f'| Orchid watering - {orchid_2.wateringUnder()}')
print('')
print(f'| Name - {orchid_3.name} | Tribe - {orchid_3.tribe} | Cor - {orchid_3.color} |')
print(f'| Orchid watering - {orchid_3.wateringUnder()}')