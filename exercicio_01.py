# Exercício nº 1 do processo seletivo para vaga de estágio na Target Sistemas

# Observe o trecho de código abaixo:
# int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k
    print(soma)

# O valor final da variável SOMA será 91.
