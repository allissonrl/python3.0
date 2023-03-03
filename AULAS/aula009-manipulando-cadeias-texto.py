frase ='Curso em Video Python'
fat = 'Fatiamento'
anal = 'ANALISE'
print(frase)
print(f'{fat:=^20}')
print(f'Usando o fatiamento frase[9] = {frase[9]}')
print(f'Fatiamento começo e fim, frase[9:13] = {frase[9:14]}')
print(f'Outro Exemplo Fatiamento, frase[9:21] = {frase[9:21]}\n')

print(f'{fat:=^20} pulando 2 casas')
print(f'Começa, Termina, e pula... = {frase[9:21:2]}\n')

print(f'{fat:=^20} Onde ele começa e onde ele termina')
print(f'Onde começa e onde termina frase [:5] = {frase[:5]}')
print(f'Outro exemplo frase [15:] = {frase[15: ]}')
print(f'Começa do 9 vai ate o final pulando 3 casas FRASE [9::3] = {frase[9::3]}\n\n')

print(f'FAtiamento  {anal:=^20}')
print(f'mostrar o comprimento da frase usa len(frase) = {len(frase)} caracteres')
print(f'A funcao frase.count(o) conta letras o tem, = {frase.count("o")} letras\n\n')

print('Contagem de letras com fatiamento')
print(f'Conta quantas letras o tem dentro de um fatiamento  {frase.count("o",0,13)}')
print('frase.count("o",0,13) -> vai do começo ate o caracter 13, no ultimo valor ignorado \n')

print(f'Procurar onde começa  o caracter ou palavras -> frase.find("deo") = {frase.find("deo")}')
print(f'se colocar caracter ou palavras que não exista apararecera o -1 = frase.find("android") = {frase.find("android")}\n\n')

print('OPERADOR "IN')
print(f'Exemplo "Curso" in frase... a palavra curso tem em frase -> {"Curso" in frase}\n\n')

print(f'{fat:=^20} TRANSFORMAÇÃO')

print(f' frase.replace("Python", "Android") troca uma palavra para outra => {frase.replace("Python", "Android")}')
print(f'frase.upper(), transforma a palavra ou a frase toda em MAIUSCULA => {frase.upper()}')
print(f'frase.lower, transforma a palavra ou a frase toda em minuscula => {frase.lower()}')
print(f'frase.capitalize(), transforma a palavras ou a frase toda em minuscula e coloca.'
      f'o primeiro caracter em MAIUSCULA => {frase.capitalize()}')
print(f'frase.title(), analiza uma string inteira e coloca a primeira palavra '
      f'de cada letra em MAIUSCULA => {frase.title()}')
print(f'frase.strip, remove todos os espaços inuteis do começo e do fim => {frase.strip()}')
print(f'frase.rstrip, remove os espaços inuteis da direita da string => {frase.rstrip()}')
print(f'frase.lstrip, remove os espaços inuteis da esquerda da string => {frase.lstrip()}\n\n')

print(f'{fat:=^20} DIVISÃO')
print(f'frase.split(), divide a string ou a frase em partes,\n'
      f'criando uma lista com palavras separadas, e toda palavra recebe uma indexação nova => {frase.split()}\n')

print(f'{fat:=^20} JUNÇÃO')

print(f'depois que usar o split para separa, usar o join para juntar => {"-".join(frase).replace("-","")}')

