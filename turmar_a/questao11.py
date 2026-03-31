alunos = []

for i in range(15):
    n1, n2, n3, n4, nome = input().split()
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)

    media = (n1 + n2 + n3 + n4) / 4
    if media >= 6:
        situa = 'Aprovado'
    elif 4 <= media < 6:
        situa = 'Recuperação'
    else:
        situa = 'Reprovado'
    
    aluno = f'{n1};{n2};{n3};{n4};{media};{situa};{nome}'
    alunos.append(aluno)

for aluno in alunos:
    print(aluno)
