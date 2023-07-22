print('Olá, Mundo!')

mensagem = 'Olá, Mundo!'
print(mensagem)

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}! Você se tornará um(a) grande desenvolvedor(a).'.format(nome))

nome = input('Digite seu nome: ')
print(f'É um prazer te conhecer, {nome}! Você se tornará um(a) grande desenvolvedor(a).')

num1 = (input('Digite o primeiro número: '))
num2 = (input('Digite o segundo número: '))
soma = num1 + num2
print(f'A soma entre {num1} + {num2} é {num1 + num2}')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = num1 + num2
print(f'A soma entre {num1} + {num2} é {num1 + num2}')

algo = input('Digite algo: ')
print(algo,'É do tipo primitivo', type(algo))
print(algo,'Possui apenas números?', algo.isnumeric())
print(algo,'Possui apenas letras?', algo.isalpha())
print(algo,'Possui letras e/ou números?', algo.isalnum())
print(algo,'Possui números de 0 a 9?', algo.isdecimal())
print(algo,'Possui todos as palavras em minúsculo?', algo.islower())
print(algo,'Possui apenas espaços em branco?', algo.isspace())
print(algo,'Possui apenas letras maiúsculas?', algo.isupper())
print(algo,'Possui a primeira palavra maiúscula e o restante minúsculas?',algo.istitle())

