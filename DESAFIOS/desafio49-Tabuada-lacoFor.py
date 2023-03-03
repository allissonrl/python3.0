from cores import textovermelho,textamarelo,textoazul,textociano,textoverde,fecha,fundoAzul
num = int(input('Digite um numero : '))
print('='*5,end='')
print(f'{textovermelho}TABUADA{fecha}',end='')
print('='*5)
cont = 0
for c in range(1,11):
    print(f'{num} X {c:>2} = {num*c:>2}')