n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))
n4 = float(input("Numero 4: "))

media = (n1+n2+n3+n4) / 4

numeros = [n1, n2, n3, n4]
diferenca = max(numeros) - min(numeros)

print(f"A média aritmética é: {media}")
      
print(f"A diferença entre o maior e o menor valor é: {diferenca}")