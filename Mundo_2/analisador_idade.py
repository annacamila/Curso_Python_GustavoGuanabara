#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
media_idade = 0
maior_idade_masc = 0
nome_velho = ''
mulher20 = 0
for pessoa in range(1,5):
    print(f'----- {pessoa}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mn':
        maior_idade_masc = idade
        nome_velho = nome
    if sexo in 'Mn' and idade > maior_idade_masc:
        maior_idade_masc = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

media_idade = soma_idade / 4

print(f'A media de idade do grupo e de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_masc} anos e se chama {nome_velho}.')
print(f'Ao todo sao {mulher20} mulheres com menos de 20 anos.')
