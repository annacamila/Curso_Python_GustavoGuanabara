#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
nome = ('Ana Camila Santos').strip()
print(f'Nome em maiúsculas {nome.upper()}')
print(f'Nome em minúsculas {nome.lower()}')
print(f"Quantidade de letras ao todo, sem os espacos {len(nome) - nome.count(' ')}")
print(f"Quantidade de letras primeiro nome {nome.find(' ')}")
separa_nome = nome.split()
print(separa_nome)
print(f'O primeiro nome é {separa_nome[0]} e ele tem {len(separa_nome[0])} letras')
nome_oab = ('Leonardo Silva - MG112423')
nome_oab_separados = nome_oab.split('-')
print(nome_oab_separados)
print(nome_oab_separados[1])
print(nome_oab_separados[1].strip())

#Faça um programa que leia uma frase e mostre quantas vezes aparece a letra “A”, em que posição ela aparece, a primeira vez e em que posição ela aparece a última vez.
frase = ('O sucesso é a soma de pequenos esforços repetidos dia após dia').upper()
print(f"A letra A aparece {frase.count('A')} vezes na frase")
print(f"A primeira letra A apareceu na posicao {frase.find('A')+1}")
print(f"A ultima letra A apareceu na posicao {frase.rfind('A')+1}")

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome_completo = ('Ana Camila Santos')
print(nome_completo)
divida_nome = nome_completo.split()
print(divida_nome)
print(f'O primeiro nome é {divida_nome[0]}')
print(f'O ultimo nome é {divida_nome[-1]}')
