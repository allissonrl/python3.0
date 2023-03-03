nome = str(input('Digite seu nome complete: ')).strip()
nomeCortado = nome.split()
primeiroNone = nomeCortado[0]
ultimoNome = nomeCortado[-1]

print(f'PRIMEIRO NOME = {primeiroNone}')
print(f'ULTIMO NOME = {ultimoNome}')