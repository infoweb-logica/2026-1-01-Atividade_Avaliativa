alunos= []

for i in range(15):
    dados=input('Notas e nome do aluno: ').split()
    n1=float(dados[0])
    n2=float(dados[1])
    n3=float(dados[2])
    n4=float(dados[3])
    nome=''.join(dados[4:])
    media= (n1+n2+n3+n4) / 4
    if media >= 6:
        resultado='Aprovado'
    elif media == 4 and media > 6:
        resultado='Recuperação'
    else:
       resultado='Reprovado'
    alunos.append([nome, n1,n2,n3,n4, media, resultado])
    
for aluno in alunos:
    print(f'{aluno[1]}; {aluno[2]}; {aluno[3]}; {aluno[4]} ; {aluno[0]}; {aluno[5]}; {aluno[6]}')