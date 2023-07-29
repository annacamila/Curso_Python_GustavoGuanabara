#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = mais1000 = mais_barato = contador = 0
nome_barato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco: R$ '))
    contador += 1
    total += preco
    if preco > 1000:
        mais1000 += 1
    if contador == 1 or preco < mais_barato:
        mais_barato = preco
        nome_barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total gasto na compra foi R${total:.2f}')
print(f'{mais1000} produtos custam mais de R$1000,00.')
print(f'O produto mais barato e o(a) {nome_barato} que custa R${mais_barato:.2f} ')

