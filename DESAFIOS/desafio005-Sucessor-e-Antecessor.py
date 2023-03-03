textovermelho = '\033[31m'
textoverde = '\033[32m'
textamarelo = '\033[33m'
textoazul = '\033[34m'
textociano = '\033[36m'
verdesubliando = '\033[4;32m'
fundoAzul = '\033[44m'
fecha = '\033[m'
num = int(input('Digite um numero: '))
print(f'o seu sucessor é {textoverde} {num+1} {fecha} e o seu antecessor é{textamarelo} {num-1}.{fecha}')
