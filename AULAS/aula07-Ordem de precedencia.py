"""print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)

nome = input('Qual é o seu nome: ')
print(f'Prazer em te conhecer {nome:=^20}!')"""""

n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
soma = n1 + n2
multiplicação = n1 * n2
divisão = n1 / n2
divisaoInteria = n1 // n2
potencia = n1 ** n2

print(f'A soma é {soma}, \n o produto é {multiplicação}, \n e a divisão é {divisão:.2f}', end=' ')
print(f'Divição inteira é {divisaoInteria} e Potencia {potencia}')