# Crie um algoritmo que leia um núm e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print(f'O dobro é {d}\nO triplo é {t}\nA raiz quadrada é {r:.3f}')
