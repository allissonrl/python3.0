from random import shuffle
import cores
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome de outro aluno: '))
n3 = str(input('digite o nome do outro aluno: '))
n4 = str(input('digite o nome do aluno: '))
listaalunos = [n1, n2,n3,n4]
shuffle(listaalunos)
print(f'{cores.textoverde}A ordem de apresentação é {listaalunos}{cores.fecha}')