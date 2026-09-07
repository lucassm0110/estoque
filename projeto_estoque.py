produtos = []

def cadastrar_produto(produtos):
    print("\n===== CADASTRAR PRODUTO =====")

    nome = input("Digite o nome do produto: ")

    preco = float(input("Digite o preço do produto: ").replace(",", "."))    
    quantidade = int(input("Digite a quantidade em estoque: "))
    produto = [nome, preco, quantidade]

    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!")


def listar_produtos(produtos):
    print("\n===== LISTA DE PRODUTOS =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for i, produto in enumerate(produtos):
        preco = f"{produto[1]:.2f}".replace(".", ",")

        print(f"\nProduto {i + 1}")
        print("Nome:", produto[0])
        print("Preço: R$", preco)
        print("Quantidade:", produto[2])


def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto[0].lower() == nome.lower():
            return produto

    return None


def entrada_estoque(produtos):
    print("\n===== ENTRADA DE ESTOQUE =====")

    nome = input("Digite o nome do produto: ")

    produto = buscar_produto(produtos, nome)

    if produto is None:
        print("\nProduto não encontrado.")
        return

    quantidade = int(input("Digite a quantidade de entrada: "))

    if quantidade <= 0:
        print("\nA quantidade deve ser maior que zero.")
        return

    produto[2] += quantidade

    print("\nEntrada realizada com sucesso!")
    print("Nova quantidade em estoque:", produto[2])


def saida_estoque(produtos):
    print("\n===== SAÍDA DE ESTOQUE =====")

    nome = input("Digite o nome do produto: ")

    produto = buscar_produto(produtos, nome)

    if produto is None:
        print("\nProduto não encontrado.")
        return

    print("Quantidade disponível:", produto[2])

    quantidade = int(input("Digite a quantidade de saída: "))

    if quantidade <= 0:
        print("\nA quantidade deve ser maior que zero.")
        return

    if quantidade > produto[2]:
        print("\nEstoque insuficiente.")
        return

    produto[2] -= quantidade

    print("\nSaída realizada com sucesso!")
    print("Nova quantidade em estoque:", produto[2])


def calcular_valor_estoque(produtos):
    print("\n===== VALOR TOTAL DO ESTOQUE =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    valor_total = 0

    for produto in produtos:
        valor_total += produto[1] * produto[2]

    valor_formatado = f"{valor_total:.2f}".replace(".", ",")

    print("Valor total do estoque: R$", valor_formatado)


# DESAFIO ADICIONAL

def maior_estoque(produtos):
    print("\n===== PRODUTO COM MAIOR QUANTIDADE =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    maior = produtos[0]

    for produto in produtos:
        if produto[2] > maior[2]:
            maior = produto

    print("Produto:", maior[0])
    print("Quantidade:", maior[2])


def menor_estoque(produtos):
    print("\n===== PRODUTO COM MENOR QUANTIDADE =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    menor = produtos[0]

    for produto in produtos:
        if produto[2] < menor[2]:
            menor = produto

    print("Produto:", menor[0])
    print("Quantidade:", menor[2])


def produto_mais_caro(produtos):
    print("\n===== PRODUTO MAIS CARO =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    mais_caro = produtos[0]

    for produto in produtos:
        if produto[1] > mais_caro[1]:
            mais_caro = produto

    preco = f"{mais_caro[1]:.2f}".replace(".", ",")

    print("Produto:", mais_caro[0])
    print("Preço: R$", preco)


def estoque_baixo(produtos):
    print("\n===== PRODUTOS COM ESTOQUE BAIXO =====")

    encontrou = False

    for produto in produtos:
        if produto[2] < 5:
            print("\nProduto:", produto[0])
            print("Quantidade:", produto[2])

            encontrou = True

    if not encontrou:
        print("Nenhum produto possui estoque baixo.")



while True:
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Entrada de estoque")
    print("5 - Saída de estoque")
    print("6 - Mostrar valor total do estoque")
    print("7 - Mostrar produto com maior quantidade em estoque")
    print("8 - Mostrar produto com menor quantidade em estoque")
    print("9 - Mostrar produto mais caro")
    print("10 - Mostrar listagem de produtos com estoque baixo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto(produtos)

    elif opcao == "2":
        listar_produtos(produtos)

    elif opcao == "3":
        nome = input("Digite o nome do produto: ")
        produto = buscar_produto(produtos, nome)

        if produto == None:
            print("\nProduto não encontrado.")
        else:
            preco = f"{produto[1]:.2f}".replace(".", ",")

            print("\n===== PRODUTO ENCONTRADO =====")
            print("Nome:", produto[0])
            print("Preço: R$", preco)
            print("Quantidade:", produto[2])

    elif opcao == "4":
        entrada_estoque(produtos)

    elif opcao == "5":
        saida_estoque(produtos)

    elif opcao == "6":
        calcular_valor_estoque(produtos)

    elif opcao == "7":
        maior_estoque(produtos)

    elif opcao == "8":
        menor_estoque(produtos)

    elif opcao == "9":
        produto_mais_caro(produtos)

    elif opcao == "10":
        estoque_baixo(produtos)


    elif opcao == "0":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")
        continue

    print("\nO que deseja fazer agora?")
    print("1 - Voltar ao menu")
    print("0 - Encerrar o sistema")

    continuar = input("Escolha uma opção: ")

    if continuar == "0":
        print("\nSistema encerrado.")
        break
