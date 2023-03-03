textovermelho = '\033[31m'
textoverde = '\033[32m'
textamarelo = '\033[33m'
textoazul = '\033[34m'
textociano = '\033[36m'
verdesubliando = '\033[4;32m'
fundoAzul = '\033[44m'
fecha = '\033[m'

num = int(input('Digite um numero: '))
# a RAiz quadrada poder ser feita tambem assim ----> raiz = pow(n, (1/2))
print(f'{textoazul} O seu dobro é {num*2}, O seu triplo é {num*3}, a sua raiz quadrada é {num ** (1/2):.2f} {fecha}')
