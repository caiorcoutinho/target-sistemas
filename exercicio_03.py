# Exercício nº 3 do processo seletivo para vaga de estágio na Target Sistemas

# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
# faça um programa, na linguagem que desejar, que calcule e retorne:
# O menor valor de faturamento ocorrido em um dia do mês;
# O maior valor de faturamento ocorrido em um dia do mês;
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

# Json disponibilizado
with open('dados.json') as file: data = json.load(file)

# Inicializando pior e melhor dia para fins de teste lógico posterior
worst_day = data[0]
best_day = data[0]

# Inicializando somador para cálculo de média posterior
sum_values = 0

# Iterando, testando os valores, identificando pior e melhor dia e somando valores para cálculo de média
for day in data:
    if day['valor'] < worst_day['valor']:
        worst_day = day
    elif day['valor'] > best_day['valor']:
        best_day = day
    sum_values += day['valor']

# Cálculo de média
day_count = len([day for day in data if day['valor'] > 0.0]) # Excluindo os dias com zero vendas da contagem 
average = sum_values / day_count

# List comprehension para armazenar os dias com faturamento acima da média
over_average_revenue = [day for day in data if day['valor'] >= average]
over_average_revenue.sort(key=lambda x: x['valor'], reverse=True) # Organizando em ordem crescente

# Exibindo os resultados
print('Dia com o melhor faturamento: ')
print(f"dia: {best_day['dia']}, valor: R$ {best_day['valor']:.2f}")
print()

print('Dia com o pior faturamento: ')
print(f"dia: {worst_day['dia']}, valor: R$ {worst_day['valor']:.2f}")
print()

print(f'Dias com faturamento acima da média: ')
for item in over_average_revenue:
    print(f"dia: {item['dia']}, valor: R$ {item['valor']:.2f}")
print()
