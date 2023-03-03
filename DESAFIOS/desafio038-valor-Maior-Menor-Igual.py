num = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num > num2:
    print(f'Os numeros digitados foram {num, num2} '
          f'o primeiro numero e maior que o segundo.')
elif num < num2:
    print(f'Os numeros digitados foram {num, num2} '
          f'e o segundo numero é o maior.')
else:
    print(f'Os numeros digitados foram {num, num2}'
          f' e os dois são iguais')
