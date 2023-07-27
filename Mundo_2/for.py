#Refaça o DESAFIO 9 (Mundo01), mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input('Digite um numero para ver sua tabuada: '))
for num in range(1,11):
     #print(f'{numero} X {num} = {numero * num}') 
     print(f'{numero} X {num:2} = {numero * num}') # O ":2" é para ter dois digitos

#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar_palavras = ''.join(palavras)
frase_inverso = ''
for letra in range(len(juntar_palavras) -1, -1, -1):
    frase_inverso += juntar_palavras[letra]
print(juntar_palavras, '- ', frase_inverso)
if frase_inverso == juntar_palavras:
    print('A frase digitada e um palíndromo!')
else:
    print('A frase digitada nao e um palíndromo!')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar_palavras = ''.join(palavras)
frase_inverso = juntar_palavras[::-1]
print(juntar_palavras, '- ', frase_inverso)
if frase_inverso == juntar_palavras:
    print('A frase digitada e um palíndromo!')
else:
    print('A frase digitada nao e um palíndromo!')

