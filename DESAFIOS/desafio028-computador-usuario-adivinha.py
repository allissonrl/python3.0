from random import randint
from time import sleep
print('\033[33m-=-\033[m'*18)
print('\033[34mVou pensar em um numero entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m'*18)
print('Descubra qual o numero que o computador esta pensando!')
usuario = int(input('digite um numero: '))#jogador escolhe o numero
print('PROCESSANDO...')
sleep(3)
computador = randint(0,5) #computador pensando
if usuario == computador:
    print(f'o computador pensou {computador}')
    print('\033[1;32mVOCE ACERTOU\033[m')
else:
    print(f'O computador pensou {computador}')
    print('\033[1;31m VOCE PERDEU\033[m')