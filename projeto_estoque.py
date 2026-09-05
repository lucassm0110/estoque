while True:
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Entrada de estoque")
    print("5 - Saída de estoque")
    print("6 - Mostrar valor total do estoque")
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