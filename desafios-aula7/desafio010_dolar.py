# Crie um programa que leia qto dinheiro uma pessoa tem na carteira e mostre qtos dólares ela pode comprar.

n = float(input('Informe o valor em reais que possui na carteira: '))
d = (n / 3.27)
print(f'Você poderá comprar {d:.2f} dólares.')
