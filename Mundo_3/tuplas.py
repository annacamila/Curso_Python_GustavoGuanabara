#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender', 'programar', 'python', 'rpa', 
            'programadora', 'desenvolvedora', 'futuro', 'logica',
            'estudar', 'praticar', 'cafe', 'leitura')
for palavra in palavras:
    print(f'\n Na palavra {palavra.upper()} temos: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

