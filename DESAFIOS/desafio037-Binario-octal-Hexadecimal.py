
num = int(input('Digite um numero inteiro para converter: '))
frase = 'BASE CONVERSAO'
print(f'{frase:*^20}')
print("""DIGITE
[1] para converter para BINARIO
[2] para converter para OCTAL
[3] para converter para HEXADECIMAL""")
conversao = int(input('DIGITE O NUMERO PARA CONVERSÃO: '))
if conversao == 1:
    print(f'numero {num} convertido para Binario é {bin(num[2::])}')
elif conversao == 2:
    print(f'numero {num} convertido para octal é {oct(num)[2::]}')
elif conversao == 3:
    print(f'numero {num} convertido para hexadecimal é {hex(num)[2::]}')

else:
    print('opção errada')