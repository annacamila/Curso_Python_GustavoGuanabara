#Requisito: 𝐂𝐚𝐝𝐚𝐬𝐭𝐫𝐨 𝐞 𝐥𝐢𝐬𝐭𝐚𝐠𝐞𝐦 𝐝𝐞 𝐩𝐫𝐨𝐝𝐮𝐭𝐨𝐬
#𝐂𝐚𝐝𝐚𝐬𝐭𝐫𝐨:
#- Formulário com os campos abaixo:
 #- Nome do produto - campo de texto
  #- Descrição do produto - campo de texto
  #- Valor do produto - campo de valor
  #- Disponível para venda - campo com 2 opções: sim / não
#𝐋𝐢𝐬𝐭𝐚𝐠𝐞𝐦:
#- Colunas da listagem: nome, valor
#- Ordenação por valor do menor para o maior
#- Quando cadastrar um novo produto é para abrir a listagem automaticamente
#- Deve existir um botão para cadastrar um novo produto a partir da listagem

nome_produto = []
descricao_produto = []
valor_produto = []
disponivel_venda = []


def cadastrar_produto():
    print("Cadastro de Produtos: ")
    nome = input("Digite o nome do produto: ")
    descricao = input("Qual a descrição do produto?: ")
    valor = float(input("Digite o valor do produto: "))
    disponivel = input("Produto disponível para venda? (sim/não): ").lower()
    
    nome_produto.append(nome)
    descricao_produto.append(descricao)
    valor_produto.append(valor)
    disponivel_venda.append(disponivel)
    
    print("Produto cadastrado com sucesso!")


def listar_produtos():
    print("Lista de Produtos: ")
    
    produtos_ordenados = sorted(zip(nome_produto, valor_produto), key=lambda x: x[1])
    
    for nome, valor in produtos_ordenados:
        print(f"Nome: {nome}")
        print(f"Valor: {valor}\n")
    
    input("Pressione Enter para continuar...")


while True:
    print("Cadastro e Listagem de Produtos")
    print("1 - Cadastrar Novo Produto")
    print("2 - Listar Produtos")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        print("Saindo do programa. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")
