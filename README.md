# 2026 - ILP - Atividade avaliativa no. 1 do 1o bimestre

## Informações gerais
- **Objetivo**: FIXME
- **Público alvo**: alunos da disciplina de [Introdução a lógica e programação](https://github.com/infoweb-logica/) do curso de [Infoweb](https://diatinf.ifrn.edu.br/cursos/tecnico-em-informatica-para-internet/) na [DIATINF](https://diatinf.ifrn.edu.br/) no [CNAT-IFRN](https://portal.ifrn.edu.br/campus/natalcentral/)
- **Professor**: [L A Minora](https://github.com/leonardo-minora/)
- **Aluno(a)(e)**: [Leonardo Ataide Minora](https://github.com/leonardo-minora)

---

## Checklist

- [X] 1. Fork desse repositório
- [X] 2. Substitui neste arquivo (`README.md`) de `FIXME` pelo seu nome
- [X] 3. Abrir o VS Code local ou o _codespaces_ para criar os arquivos respostas da avaliação. Preferível o _codespaces_.
- [ ] 4. Responder as questões abaixos.
- [ ] 5. Publicar no Github suas repostas.

> 💡 **Dica 01:** Preste atenção nos nomes dos arquivos especificados no texto das questões.

> 💡 **Dica 02:** Lembre de publicar suas respostas no Github de votla, se não eu não consigo acessar suas respostas.

> 💡 **Dica 03:** Dúvidas, pergunte!!! Estamos todos aprendendo.

---

## Lista de questões

### Questão 1
Escreva um programa Python que exiba na tela a mensagem `Bom dia família infoweb 2026!`.

**Arquivo resposta**: `questao01.py`

---

### Questão 2
Escreva um programa Python que exiba na tela as seguintes três linhas:
```
Meu nome é Fulano.
Tenho 18 anos.
Estou no curso de Informática para Internet.
```

**Arquivo resposta**: `questao02.py`

---

### Questão 3
Escreva um programa Python que exiba na tela as seguintes cinco linhas:
```
*** Cardápio ***
1. Pizza
2. Hambúrguer
3. Suco
*** Bom apetite! ***
```

**Arquivo resposta**: `questao03.py`

---

### Questão 4
Escreva um programa Python que leia o **nome** e a **cidade** do usuário e exiba uma mensagem de boas-vindas usando f-string.

Exemplo de entrada:
```
Ana
Natal
```

Exemplo de saída:
```
Bem-vinda(o) a avaliação de ILP, Ana! Você é de Natal.
```

**Arquivo resposta**: `questao04.py`

---

### Questão 5
Escreva um programa Python que leia o **nome** e o **curso** do usuário e exiba uma mensagem de apresentação usando f-string.

Exemplo de entrada:
```
Carlos
Infoweb
```

Exemplo de saída:
```
Olá! Meu nome é Carlos e estou matriculado no curso Infoweb.
```

**Arquivo resposta**: `questao05.py`

---

### Questão 6
Escreva um programa Python que leia **4 números inteiros** e exiba a soma e o produto deles usando f-string.

Exemplo de entrada:
```
2
3
4
5
```

Exemplo de saída:
```
A soma dos números é: 14
O produto dos números é: 120
```

**Arquivo resposta**: `questao06.py`

---

### Questão 7
Escreva um programa Python que leia **4 números reais** e exiba a média aritmética e a diferença entre o maior e o menor valor usando f-string.

Exemplo de entrada:
```
10.0
6.0
8.0
4.0
```

Exemplo de saída:
```
A média aritmética é: 7.0
A diferença entre o maior e o menor valor é: 6.0
```

**Arquivo resposta**: `questao07.py`

---

### Questão 8
Escreva um programa Python que leia **4 números inteiros** e use o `if` para verificar se a soma deles é maior que 100. Exiba dois prints usando f-string: um com o valor da soma e outro informando se ela é maior que 100 ou não.

Exemplo de entrada:
```
30
40
20
15
```

Exemplo de saída (quando a soma for maior que 100):
```
A soma dos 4 números é: 105
A soma é maior que 100.
```

**Arquivo resposta**: `questao08.py`

---

### Questão 9
Escreva um programa Python que leia **4 números reais** e use o `if` para verificar se o produto deles é positivo. Exiba dois prints usando f-string: um com o valor do produto e outro indicando se ele é positivo ou não.

Exemplo de entrada:
```
2.0
3.0
-1.0
4.0
```

Exemplo de saída (quando o produto não for positivo):
```
O produto dos 4 números é: -24.0
O produto não é positivo.
```

**Arquivo resposta**: `questao09.py`

---

### Questão 10
Escreva um programa Python que leia **4 números inteiros** e use o `if else` para verificar se a média deles é maior ou igual a 6. Exiba dois prints usando f-string: um com o valor da média e outro indicando se o aluno foi aprovado (média ≥ 6) ou reprovado (média < 6).

Exemplo de entrada:
```
8
5
7
6
```

Exemplo de saída (quando aprovado):
```
A média é: 6.5
Situação: Aprovado(a)!
```

**Arquivo resposta**: `questao10.py`

---

### Questão 11 — Desafio 🏆
Escreva um programa Python que leia para 15 alunos uma série de **4 números inteiros** e o **nome do aluno** representando as notas em 4 bimestres de um aluno. O programa deve:
1. Calcular a média das notas.
2. Usar `if else` para determinar a situação: **Aprovado** (média ≥ 6), **Recuperação** (4 ≤ média < 6) ou **Reprovado** (média < 4).
3. Usar um laço `while` ou `for` para percorrer os dados dos alunos e imprimir cada uma no formato de linha CSV (separadas por `;` e com `end=';'`), exibindo ao final a média e a situação também separadas por `;`.

Exemplo de entrada:
```
7 5 8 6 Fulano
7.1 5.2 8.3 6.4 Cicrano
7 5 8 6 FulanoCicrano
7.1 5.2 8.3 6.4 CicranoFulano
1 2 3 4 CFulano
4 3 2 1 FCicrano
4 4 4 4 CF
5.9 5.9 5.9 5.9 FC
...
```

Exemplo de saída:
```
7;5;8;6;6.5;Aprovado;Fulano
7.1;5.2;8.3;6.4;6,75;Aprovado;Cicrano
7;5;8;6;6.5;Aprovado;FulanoCicrano
7.1;5.2;8.3;6.4;6.75;Aprovado;CicranoFulano
1;2;3;4;2.5;Reprovado;CFulano
4;3;2;1;2.5;Reprovado;FCicrano
4;4;4;4;4.0;Recuperação;CF
5.9;5.9;5.9;5.9;5.9;Recuperação;FC
...
```

>;**Dica**: se preferir no lugar de fazer `print(valor, end=';')` use f-string para imprimir sem quebra de linha e separando os valores com `;`.

**Arquivo resposta**: `questao11.py`

## Sintaxe python

```python
nota_1 = 1
nota_2 = 2

if nota_1 > nota_2:
    print("nota 1 maior que nota 2")

if nota_1 == nota_2:
    print("nota 1 igual a nota 2")

if nota_1 < nota_2:
    print("nota 1 menor que 2")

if nota_1 > 0:
    print("nota 1 é números positivo")
elif nota_1 < 0:
    print("nota 1 é números negativo")
else:
    print("nota 1 é igual a zero")

if nota_1 > 0 and nota_2 > 0:
    print("ambas a notas são números positivos")
```
