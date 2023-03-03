textovermelho = '\033[31m'
textoverde = '\033[32m'
verdesubliando = '\033[4;32m'
fecha = '\033[n'

n1 = int(input('digite um numero: '))
n2 = int(input('digite mais um numero: '))
soma = n1 + n2
print(f'A soma de {textovermelho}{n1}{fecha} e {textovermelho}{n2}{fecha} vale: {textoverde} {soma} {fecha}')
