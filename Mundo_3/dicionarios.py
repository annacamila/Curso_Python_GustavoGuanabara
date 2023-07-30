from datetime import datetime

#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (Não tem == 0): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario R$: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35 - datetime.now().year))
print('-=' * 30)
for chave, valor in dados.items():
    print(f'  - {chave} tem o valor: {valor}')

#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for quant_partidas in range(0 , total_partidas):
    partidas.append(int(input(f'Quantos gols nas partidas {quant_partidas + 1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
for chave, valor in jogador.items():
    print (f'{chave} tem o valor {valor}')
print(f' O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for item, valor in enumerate(jogador['gols']):
    print(f'  => Na partida {item + 1}, fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média.
galera = []
pessoa ={}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: M/F ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? S/N: ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')  
    if resposta == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for pessoa in galera:
    if pessoa['sexo'] in 'F':
        print(f'{pessoa["nome"]} ', end='')
print()
print('Lista de pessoas com idade acima da média: ')
for pessoa in galera:
    if pessoa['idade'] >= media:
        print('     ', end='')
        for chave, valor in pessoa.items():
            print(f'{chave} = {valor}: ', end='')
        print()
print('<< ENCERRADO >>')

