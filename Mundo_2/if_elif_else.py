from datetime import date
from random import randint
from time import sleep


#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento sera em {ano}')
#elif idade > 18:
else:
    saldo = idade - 18
    print(f'Voce ja deveria ter se alistado há {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')


#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros
print(f'{"LOJAS ANA CAMILA":=^40}')
preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual opcao de pagamento? '))
if opcao ==  1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra sera parcelada em 2X de R${parcela:.2f}, SEM JUROS.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print(f'Sua compra sera parcelada em {total_parcelas}X de R${parcela:.2f}, COM JUROS.')
else:
    total = preco
    print('Opcao de pagamento INVALIDA, escolha uma opcao valida.')

print(f'Sua compra de R${preco:.2f}, vai custar R${total:.2f}.')


#Crie um programa que faça o computador jogar Jokenpô com você. (GAME: Pedra, Papel e Tesoura)
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')

computador = randint(0 , 2)
#print(f'O computador escolheu {opcoes[computador]}')
print('''Suas opcoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

jogador = int(input('Qual a sua escolha? '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA!')
else:
    print('-=' * 11)
    print(f'Computador escolheu {opcoes[computador]}')
    print(f'Jogador escolheu {opcoes[jogador]}')
    print('-=' * 11)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('JOGADOR GANHOU')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATOU')
      
