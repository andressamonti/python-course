# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

f = input('Digite o nome do aluno:')
n1 = float(input('Insira o valor da avaliação 1: '))
n2 = float(input('Insira o valor da avalição 2: '))
m = ((n1 + n2) / 2)
print(f'A média das avaliações do aluno {f} é {m}')
