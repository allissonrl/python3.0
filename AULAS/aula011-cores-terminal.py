print('\033[1;30;41m TESTE \033[m\n')
print('\033[4;33;44m TESTE \033[m\n')
print('\033[1;35;43m TESTE \033[m\n')
print('\033[1;30;42m TESTE \033[m\n')
print('\033[1;30;0m TESTE \033[m\n')
print('\033[mTESTE\033[m')
print('\033[7;30m TESTE \033[m\n\n')

nome = 'allisson'
cores = {'azulsumbliado' : '\033[4;34m',
        'fechamento':'\033[m'}


print(f'{cores["azulsumbliado"]} {nome}!!! {cores["fechamento"]}')