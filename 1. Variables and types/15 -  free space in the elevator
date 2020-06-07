# Fridge and elevator have = width / height / depth
# The fridge is brought to the elevator. How much free space is left in the elevator?

print('******** DIMENSIONS - FRIDGE ********')
widthFridge = float(input(('Enter the width of the fridge: ')))
heightFridge = float(input(('Enter the height of the fridge: ')))
depthFridge = float(input(('Enter the depth of the fridge: ')))
print('')

print('******** DIMENSIONS - ELEVATOR ********')
widthElevator = float(input(('Enter the width of the elevator: ')))
heightElevator = float(input(('Enter the height of the elevator: ')))
depthElevator = float(input(('Enter the depth of the elevator: ')))
print('')

volumeFridge = widthFridge * heightFridge * depthFridge
volumeElevator = widthElevator * heightElevator * depthElevator

print(f'Fridge volume" {volumeFridge} m3')
print(f'Elevator volume" {volumeElevator} m3')

spaceFree = volumeElevator - volumeFridge

if spaceFree < 0 or widthElevator < widthFridge or heightElevator < widthFridge:
    print('The fridge will not fit in the elevator.')

else:
    print(f'{round(spaceFree, 2)} - free space left in the elevator.')
