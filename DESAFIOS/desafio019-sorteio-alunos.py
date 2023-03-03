from random import choice
import cores
n1= str(input(f'{cores.textoazul}Digite o primeiro do  aluno: {cores.fecha}'))
n2= str(input('digite o segundo do aluno: '))
n3= str(input('digite o terceiro do aluno: '))
n4= str(input('digite o quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(escolhido)