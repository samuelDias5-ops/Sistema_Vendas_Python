import os
from produtos.cadastrar_produtos import cadastrar
estoque = []


def tela_inicial():
    while True:
        print("-" * 40)
        print("===== Tela Inicial =====\n")
        print("1- Cadastrar Produto")
        print("2- Fazer Vendas")
        print("3- Verificar quantidade em estoque")
        print("4- Sair")
        print("-" * 40)
        
        try:
            op = int(input("Escolha uma opção: "))
        except(ValueError, TypeError, KeyboardInterrupt):
            print("Opção inválida")
            continue
        else:
            try:
                continuar = input("Deseja tentar novamnete (s/n)? ").lower().strip()
            except:
                continue
            else:
                if continuar == "S".lower().strip():
                    continue
                elif continuar == "N".lower().strip():
                    break
            return op
        

def main():
    while True:
        op = tela_inicial()
        os.system('cls' if os.name == 'nt' else 'clear')
        match op:
                case 1:
                    pr = cadastrar()

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
                    
       
                    os.system('cls' if os.name == 'nt' else 'clear')


main()









