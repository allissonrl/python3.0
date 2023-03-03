from random import choice
from time import sleep

jokempo = ['pedra', 'papel', 'tesoura']
computador = choice(jokempo).strip()
print('Vamos jogar JOKEMPO')
print('Papel', 'Pedra', 'Tesoura')
jogador = str(input('Escolha uma opção:')).strip()
print('-='*20)
print('JO')
sleep(1)
print('kem')
sleep(1)
print('PO')
sleep(0.5)
print('-='*20)
if jogador == 'papel' and computador == 'papel' or jogador == 'pedra' and computador == 'pedra' \
        or jogador == 'tesoura' and computador == 'tesoura':
    print(f'O computador jogou {computador}\n e o jogador jogou {jogador}. Empatou o jogo')

if jogador == 'pedra' and computador == 'papel' or jogador == 'papel' and computador == 'tesoura' \
        or jogador == 'tesoura' and computador == 'pedra':
    print(f'o jogador jogou {jogador}\n e o computador jogou {computador}. computador  Ganhou')

if jogador == 'papel' and computador == 'pedra' or jogador == 'tesora' and computador == 'papel' \
        or jogador == 'pedra' and computador == 'tesoura':
    print(f'O jogador jogou {jogador}\n e o computador jogou {computador}. jogador GANHOU')
   
