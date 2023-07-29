from random import randint
      
#o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Tente advinhar qual foi')
acertou = False
palpites = 0
while not acertou: #enquanto acertou nao se tornar falso
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador ==  computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente de novo.')
        elif jogador > computador:
            print('Menos... Tente de novo.')
print(f'Acertou com {palpites} tentativas. PARABENS!')

#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor:'))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Escolha uma opcao: '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} + {num2} e {soma}')
    elif opcao == 2:
        produto = num1 * num2
        print(f'A multiplicacao entre {num1} X {num2} e {produto}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o maior valor e {maior}')
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao INVALIDA! Digite uma opcao valida.')
    print('=-=' * 10)
print('Fim do programa!')
            
#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Jogador jogou {jogador} e computador jogou {computador}, total de {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Jogador ganhou!')
            vitoria += 1
        else:
            print('Computador ganhou!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Jogador ganhou!')
            vitoria += 1
        else:
            print('Computador ganhou!')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER! Voce venceu {vitoria} vezes.')
