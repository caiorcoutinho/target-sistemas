# Exercício nº 5 do processo seletivo para vaga de estágio na Target Sistemas

#Escreva um programa que inverta os caracteres de um string.

def reverse_string(string):
    string = string[::-1]
    return string

string = input("Digite uma frase para ser invertida: ")

string = reverse_string(string)
print(f'String invertida: {string}')

