# Napisz program, który obliczy BMI:

mass = float(input('Proszę o podanie masy ciała w kg: '))
growth = float(input('Proszę o podanie wzrostu w m: '))
age = int(input('Proszę o podanie wieku: '))

BMI = ((mass * growth) / age) ** 2
print('Twoje BMI wynosi:', round(BMI, 2))