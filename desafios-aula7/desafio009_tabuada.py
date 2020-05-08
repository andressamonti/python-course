# Faça um programa que leia um número inteiro qlq e mostre na tela a sua tabuada

n = int(input('Digite o número que deseja saber a tabuada: '))
v = 0
print('-' * 40)
print(f'A tabuado do número {n} é:')
print('-' * 40)
while (v <= 10):
    print(f'{v} X {n} = {(v * n)}')
    v = v + 1
