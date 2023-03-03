textovermelho = '\033[31m'
textoverde = '\033[32m'
textamarelo = '\033[33m'
textoazul = '\033[34m'
textociano = '\033[36m'
verdesubliando = '\033[4;32m'
fundoAzul = '\033[44m'
fecha = '\033[m'

aluno = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2) / 2
print(f'O aluno {aluno} teve as notas {nota1} e {nota2} \nA soma foi {nota1+nota2}',end=' ')
print(f'{fundoAzul}e a media foi {fecha} {textociano} {media} {fecha}')
