pares = soma = 0
for c in range(1,6):
    num = int(input(f'digite o {c} numero: '))
    if num % 2 == 0:
        soma += num
        pares += 1
print(f'a soma dos numeros pares é {soma} => ')
