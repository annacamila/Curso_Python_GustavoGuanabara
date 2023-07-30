from random import randint

#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
maior = menor = 0
for posicao in range(0,5):
    lista.append(int(input(f'Digite um valor para a posicao {posicao}º ')))
    if posicao == 0:
        maior = menor = lista[posicao]
    else:
        if lista[posicao] > maior:
            maior = lista[posicao]
        if lista[posicao] < menor:
            menor = lista[posicao]
print('=-' * 30)
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')

#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.  
#B) Uma listagem com as pessoas mais pesadas.  
#C) Uma listagem com as pessoas mais leves.
lista_temp = []
lista_princ = []
maior_peso = menor_peso = 0
while True:
    lista_temp.append(str(input('Nome: ').upper()))
    lista_temp.append(float(input('Peso: ')))
    if len(lista_princ) == 0:
        maior_peso = menor_peso = lista_temp[1]
    else:
        if lista_temp[1] > maior_peso:
            maior_peso = lista_temp[1]
        if lista_temp[1] < menor_peso:
            menor_peso = lista_temp[1]
    lista_princ.append(lista_temp[:])
    lista_temp.clear() #limpa as informacoes da lista temporaria
    resposta = str(input('Quer continuar? S/N: '))
    if resposta in 'Nn':
        break
print(f'Os dados foram {lista_princ}')
print(f'Foram cadastradas {len(lista_princ)} pessoas.')
print(f'O maior peso foi {maior_peso} Kg. Peso de', end=' ')
for pessoas in lista_princ:
    if pessoas[1] == maior_peso:
        print(f'[{pessoas[0]}] ', end=' ')
print()
print(f'O menor peso foi {menor_peso} Kg. Peso de', end=' ')
for pessoas in lista_princ:
    if pessoas[1] == menor_peso:
        print(f'[{pessoas[0]}] ', end=' ')
print()

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
lista = []
jogos = []
quantidade = int(input('Quantos jogos quer que sorteia? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f' SORTEANDO {quantidade} JOGOS ', '-=' * 3)
for indice, listaa in enumerate(jogos):
    print(f'Jogo {indice + 1}: {listaa}')

#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
dados_aluno = []
while True:
    nome = str(input('Nome: ').upper())
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados_aluno.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? S/N '))
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 26)
for indice, alunos in enumerate(dados_aluno):
    print(f'{indice:<4}{alunos[0]:<10}{alunos[2]:>8.1f}')
while True:
    print('-=' * 30)
    opcao = int(input('Mostrar notas de qual aluno? (Interromper = 999): '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(dados_aluno) - 1:
        print(f'Notas de {dados_aluno[opcao][0]} sao {dados_aluno[opcao][1]}')

print('FIM') 
