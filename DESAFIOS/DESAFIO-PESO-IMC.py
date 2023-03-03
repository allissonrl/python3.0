peso = float(input('Qual é o seu peso Kg: '))
altura = float(input('Qual é a sua altura (m): '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'O seu IMC é {imc:.1f} e esta abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'O seu imc é {imc:.1f} e esta no peso ideal')
elif 25 <= imc < 30:
    print(f'O seu imc é {imc:.1f} e esta sobrepeso')
elif 30 <= imc < 40:
    print(f'O seu imc {imc:.1f} e esta com obesidade')
else:
    print(f'o seu imc é {imc:.1f} e esta com obesidade morbida')