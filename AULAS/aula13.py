"""laco c no intervalo(1,10)"""
print('passo')
"""pega"""
"""laco == for
    no == in
    intervalo == range"""

for c in range(1,10):
    print('passo')
print('pega')

"""COM MOEDAS"""
"""laco c no intervalo(0,3)
    passo
    pula
passo
pega"""
""""==============================="""
"""laco c no intervalo(0,3)
     se moeda  => o se dentro do for
        pega
     passo
     pula
   passo
   pega"""
for c in range(0,3):
    if 'moeda':
        print('pega')
    'passo'
    'pula'
'passo'
'pega'



s = 0
for c in range(0,3):
    n = int(input(f'Digite o {c+1} valor: '))
    s += n

print(f'O somatorio de todos os numeros é {s}')

