from random import randint

tempo = int(input('Quantos anos tem seu carro:? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

tempo = int(input('Quantos anos tem seu carro:? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')

#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
computador = randint(0 , 5) #Faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer.')
else:
    print(f'GANHEI! eu pensei no numero {computador} e nao no {jogador}')

#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
     print('MULTADO! Voce excedeu o limite permitido que é de 80km/h')
     multa = (velocidade - 80) * 7
     print(f'Voce deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')

#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Que ano voce quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} nao é BISSEXTO.')

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = int(input('Qual e o salario do funcionario? R$ '))
if salario <= 1250:
    novo_salario = salario + (salario * 15 / 100)
else:
    novo_salario = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f} agora.')
