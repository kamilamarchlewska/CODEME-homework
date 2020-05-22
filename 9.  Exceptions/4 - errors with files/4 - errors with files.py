# Wywołaj błąd związany z otwarciem pliku.
# Spróbuj odczytać plik, który nie istnieje.
# Spróbuj odczytać wartość z pliku otwartym w trybie w
# Spróbuj utworzyć plik, który już istnieje w trybie x
# Obsłuż w dowolny sposób każdy z powyższych błędów.

def openFileMechanics(filename):
    with open(filename, 'r') as cat:
        lines = cat.readlines()

        for l in range(len(lines)):
            print(lines[l], end=' ')

def readingFileMechanics(filename):
    with open(filename, 'w') as cat:
        lines = cat.readlines()

        for l in range(len(lines)):
            print(lines[1], end='')

def writeFileMechanics(filename):
    with open(filename, 'x') as cat:
        cat.write('Cat Misio')



def errorReadingR(filename):
    try:
        openFileMechanics(filename)

    except FileNotFoundError:
        print('FileNotFoundError.')
        print('Invalid file name.')

    except PermissionError:
        print('PermissionError.')
        print('Invalid file name.')

def errorReadingW(filename):
    try:
        readingFileMechanics(filename)

    except Exception:
        print('Error')
        print('Incorrect reading.')

    else:
        print('')

def errorWriteX(filename):
    try:
        writeFileMechanics(filename)

    except PermissionError:
        print('PermissionError')
        print('Invalid file name.')
    except FileExistsError:
        print('FileExistsError')
        print('Invalid file name.')
    else:
        print('Invalid file name.')


print('*****  Error handling  *****')
firstNameFile = input('Provide the file name: ')
errorReadingR(firstNameFile)
print('')

secondNameFile = input('Provide the file name: ')
errorReadingW(secondNameFile)
print('')

thirdNameFile = input('Provide the file name: ')
errorWriteX(thirdNameFile)


