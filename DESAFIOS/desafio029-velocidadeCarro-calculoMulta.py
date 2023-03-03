velocidade = float(input('Digite a velocidade do carro Km/h: '))
if velocidade <= 80:
    print('\033[1;32mVelocidade dentro do permitido\033[m')
else:
    multa = (velocidade - 80) * 7
    print(f'\033[1;31m sua velocidade é \033[1;33m{velocidade}Km\h\033[m\033[1;31m , e voce foi multado em\033[m\033[n \033[1;33mR$ {multa:.2f} reais.\033[m')