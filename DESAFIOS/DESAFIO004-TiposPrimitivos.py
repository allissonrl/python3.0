textovermelho = '\033[31m'
textoverde = '\033[32m'
textamarelo = '\033[33m'
textoazul = '\033[34m'
textociano = '\033[36m'
verdesubliando = '\033[4;32m'
fundoAzul = '\033[44m'
fecha = '\033[m'

n1 = input('Digite algo: ')

print(f'{textovermelho} ele e alfabetico {n1.isalpha()}')
print(f'{textoverde}Ele é todo letra Maiuscula {n1.isupper()}')
print(f'{textamarelo}É alfanumerico {n1.isalnum()}')
print(f'{textoazul}tipo de variavel {type(n1)}')
print(f'{textociano}Só em espaço {n1.isspace()}')
print(f'{fundoAzul} esta em maiuscula{n1.isupper()}')
print(f'{textovermelho}esta em minuscula {n1.islower()}')
print(f'{textoazul}Esta capitalizada {n1.istitle()}')
