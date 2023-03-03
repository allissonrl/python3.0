
r1 = float(input('digite o primeiro comprimento: '))
r2 = float(input('digite o segundo comprimento: '))
r3 = float(input('digite o terceiro comprimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Pode formar um triangulo')
else:
    print('\033[1;32;40mnão pode formar um triangulo\033[m')
