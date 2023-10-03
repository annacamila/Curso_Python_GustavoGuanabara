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
