n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
media = (n1 + n2 + n3 + n4) / 4
print(f'A média é: {media}.')
if media >= 6:
    print(f'Situação: Aprovado(a)!')
else:
    print(f'Situação: Reprovado(a)')