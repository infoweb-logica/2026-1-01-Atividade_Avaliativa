n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
media = (n1 + n2 + n3 + n4) / 4
vmax = max (n1, n2, n3, n4)
vmin = min (n1, n2, n3, n4)
print (f'A média aritmética é: {media}.')
print (f'A diferença entre o maior e o menor valor é:{vmax - vmin}')