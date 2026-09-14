import os
estoque = []

def menu_inicial():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("-" * 40)
        print("===== Tela Inicial =====\n")
        print("1- Cadastrar Produto")
        print("2- Fazer Vendas")
        print("3- Verificar quantidade em estoque")
        print("4- Sair")
        print("-" * 40)

        try:
            op = int(input("Ecolha uma opção: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            match op:
                case 1:
                    nome = input(("Digite nome do produto: "))
                    preco = float(input("Digite preço do produto: "))
                    quantidade = int(input(("Digite quantidade me estoque:")))
                    produto = {"nome": nome.lower(), "preço": preco, "quantidade": quantidade}
                    estoque.append(produto)
                    print(f"Nome: {nome}| Preço: {preco}Kz| Qtd: {quantidade}, produto cadastrado com sucesso!")
                    continuar = input("Deseja continuar (s/n)? ")
                    if continuar == "s":
                        continue
                    elif continuar == "n":
                        break
                    os.system('cls' if os.name == 'nt' else 'clear')

                case 2:
                    produto = input("Digite o nome do produto que deseja comprar: ").lower()
                    produto_encontrado = None
                    for item in estoque:
                        if item["nome"] == produto:
                            produto_encontrado = item
                            break
                    if produto_encontrado:
                        preco_unidade = produto_encontrado["preço"]
                        print(f"Produto: {produto_encontrado['nome'].capitalize()} | Valor: {preco_unidade}Kz.")

                        valor = float(input("Digite o valor a pagar: "))
                        if valor >= preco_unidade:
                            troco = valor - preco_unidade
                            quantidade -= 1

                            print(f"compra efetuada com sucesso! Seu troco é de {troco}Kz. Volte sempre!")

                        elif valor < preco_unidade:
                                print(f"Valor insuficiente| O produto custa {preco_unidade}Kz.")
                        continuar = input("Deseja continuar (s/n)? ")
                        if continuar == "s":
                            continue
                        elif continuar == "n":
                            break
                        os.system('cls' if os.name == 'nt' else 'clear')

                case 3:
                    busca = input("Digite o nome do produto que deseja procurar: ").lower()
                    achou = False
                    for item in estoque:
                        if item["nome"] == busca:
                            print("-" * 30)
                            print("Produto encontrado!")
                            print(f"Nome: {item['nome'].capitalize()}")
                            print(f"Preço: {preco}Kz")
                            print(f"Qtd: {quantidade}")
                            print("-" * 30)
                            achou = True
                            break
                    if not achou:
                        print(f"\n O produto '{busca}' não foi encontrado no estoque.")
                    continuar = input("Deseja continuar (s/n)? ")
                    if continuar == "s":
                        continue
                    elif continuar == "n":
                        break
                    os.system('cls' if os.name == 'nt' else 'clear')

                case 4:
                    print("Saindo...")
                    break

                case _:
                    print("Opção incorreta.")
                    
        except(ValueError, TypeError, KeyboardInterrupt):
                    print("Opção inválida")
                    continuar = input("Deseja tentar novamnete (s/n)? ")
                    if continuar == "s":
                        continue
                    elif continuar == "n":
                        break
                    os.system('cls' if os.name == 'nt' else 'clear')


menu_inicial()









