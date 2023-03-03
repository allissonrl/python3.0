import cores
num = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
num3 = int(input('digite mais um numero: '))
lista = [num, num2,num3]
"""if num < num2 < num3:
    print(f'O menor numero é {num} e o maior é {num3}')
elif num2 < num3 < num:
    print(f'O maior numero é {num} e o menor é {num2}')
else:
    print(f'O menor numero é {num3} e maior numero é {num2}')"""
print(f'{cores.fundoAzul}{cores.textoverde}O menor numero é {min(lista)} e o maior é {max(lista)}{cores.fecha}')
