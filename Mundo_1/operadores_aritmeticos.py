#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
numero = int(input('Digite um numero: '))
antecessor = numero - 1
sucessor = numero + 1
print(f'Analisando o numero: {numero}, seu antecessor é: {antecessor} e o seu sucessor é: {sucessor}.')

#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Digite um numero: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)
print(f'O dobro de {numero}, é: {dobro}.')
print(f'O triplo de {numero}, é: {triplo}.')
print(f'A raiz quadrada de {numero}, é: {raiz_quadrada}.')

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media= (nota1 + nota2) / 2
print(f'A media entre {nota1} e {nota2} é {media}')

#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor = float(input('Digite um valor em metros: '))
cm = valor * 100
mm = valor * 1000
print(f'O valor de {valor}m, corresponde a {cm}cm e {mm}mm.')

#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
numero = int(input('Digite um numero para ver sua tabuada: '))
print(f'{numero} X {1} = {numero * 1}')
print(f'{numero} X {2} = {numero * 2}')
print(f'{numero} X {3} = {numero * 3}')
print(f'{numero} X {4} = {numero * 4}')
print(f'{numero} X {5} = {numero * 5}')
print(f'{numero} X {6} = {numero * 6}')
print(f'{numero} X {7} = {numero * 7}')
print(f'{numero} X {8} = {numero * 8}')
print(f'{numero} X {9} = {numero * 9}')
print(f'{numero} X {10} = {numero * 10}')
