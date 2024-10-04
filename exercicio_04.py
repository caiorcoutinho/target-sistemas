# Exercício nº 4 do processo seletivo para vaga de estágio na Target Sistemas

# Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
# que cada estado teve dentro do valor total mensal da distribuidora. 

revenue = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

# Calculando faturamento total
total = 0
for k, v in revenue.items():
    total += v

sp_percentage = (revenue['SP'] / total) * 100
rj_percentage = (revenue['RJ'] / total) * 100
mg_percentage = (revenue['MG'] / total) * 100
es_percentage = (revenue['ES'] / total) * 100
outros_percentage = (revenue['Outros'] / total) * 100

print(f"""
    O faturamento total foi de R$ {total}.
    Desse valor:
    São Paulo corresponde a {sp_percentage:.2f}% (R$ {revenue['SP']:.2f});
    Rio de Janeiro corresponde a {rj_percentage:.2f}% (R$ {revenue['RJ']:.2f});
    Minas Gerais corresponde a {mg_percentage:.2f}% (R$ {revenue['MG']:.2f});
    Espírito Santo corresponde a {es_percentage:.2f}% (R${ revenue['ES']:.2f});
    e outros estados correspondem a {outros_percentage:.2f}% (R$ {revenue['Outros']:.2f}).
""")
