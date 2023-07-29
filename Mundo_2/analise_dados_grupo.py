#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

maior18 = homens = mulher_menos20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite sexo M/F: ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menos20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{maior18} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulher_menos20} mulheres tem menos de 20 anos.')
