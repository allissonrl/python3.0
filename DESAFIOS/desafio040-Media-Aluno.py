import cores
texto = 'CAlCULANDO MEDIA ALUNO'
print(f'{texto:=^30}')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 5.0:
    print(f'A sua media é {media} voce esta reprovado')
elif 5.0 < media <= 6.9:
    print(f'A sua media foi {media:.1f} e voce esta de {cores.textamarelo}recuperação{cores.fecha}')
elif media >= 7.0:
    print(f'A sua media foi {media:.1f} e voce esta APROVADO')