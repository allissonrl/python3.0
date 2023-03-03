import cores
nome = str(input('Digite o seu Nome Completo: ')).strip()
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
nomeSeparado = nome.split()
contNome = nome.replace(" ","")

print(f'{cores.textoazul}Nome em letra MAIUSCULA : {nomeMaiusculo}{cores.fecha}')
print(f'{cores.textoverde}Nome em letra minuscula : {nomeMinusculo}{cores.fecha}')
print(f'No nome {nome}, tem {len(contNome)} letras')
"PODE SER USADO TAMBEM (len(nome) - nome.count(' '), isso conta os espaços e tira tambem"
print(f'No primeiro nome é {nomeSeparado[0]} e tem {len(nomeSeparado[0])} letras')