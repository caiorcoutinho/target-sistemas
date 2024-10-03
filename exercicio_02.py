# Exercício nº 2 do processo seletivo para vaga de estágio na Target Sistemas

# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o 
# número informado pertence ou não a sequência.

n = int(input('Digite um número para saber se ele pertence ou não à sequência de fibonacci: '))

fibonacci = 0
f1 = 0
f2 = 1

while fibonacci < n:
    print(fibonacci)
    fibonacci = f1 + f2
    f1 = f2
    f2 = fibonacci

if fibonacci == n:
    print(f'O número {n} pertence à sequência de Fibonacci.')
else:
    print(f'O número {n} não pertence à sequência de Fibonacci')
