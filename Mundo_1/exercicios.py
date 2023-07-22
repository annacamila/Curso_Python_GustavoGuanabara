#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensao de {largura} * {altura} e sua area e de {area}m².')
tinta = area / 2
print(f'Para pintar essa parede, voce precisara de {tinta}l de tinta.')

#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o salario do funcionario? R$ '))
novo_salario = salario + (salario * 15 / 100)
print(f'Um funcionario que ganhava R${salario}, com 15% de aumento, passara a receber R${novo_salario}.')

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
preco_total = (dias * 60) + (km * 0.15)
print(f'O valor total a pagar é de R${preco_total:.2f}')
