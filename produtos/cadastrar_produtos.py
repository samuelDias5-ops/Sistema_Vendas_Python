import os

def pedir_nome():
    while True:
        try:
            nome = input("Insira o produto que deseja cadastrar: ").strip().lower()
        except(ValueError,TypeError, KeyboardInterrupt):
            print("Insira um nome válido")
            continue
        else:
            try:
                continuar = input("Deseja continuar (s/n)? ").lower().strip()
            except:    
                continue
            else:
                if continuar == "N".lower().strip():
                    break
            os.system('cls' if os.name == 'nt' else 'clear')


def pedir_preco():
      while True:
        try:
            preco = float(input("Insira o preco do produto: "))
        except(ValueError, TypeError):
            print("Insira um valor válido!")
            continue
        else:
            try:
                continuar = input("Deseja continuar (s/n)? ").lower().strip()
            except:    
                continue
            else:
                if continuar == "N".lower().strip():
                    break
            os.system('cls' if os.name == 'nt' else 'clear')

def pedir_qtd():
    while True:
        try:
            quantidade = int(input("Insira quantidade em estoque: "))
        except(ValueError, TypeError):
            print("Insira um valor válido!")
            continue
        else:
            try:
                continuar = input("Deseja continuar (s/n)? ").lower().strip()
            except:    
                continue
            else:
                if continuar == "N".lower().strip():
                    break
            os.system('cls' if os.name == 'nt' else 'clear')
    
def cadastrar():
    nome = pedir_nome()
    preco = pedir_preco()
    qtd = pedir_qtd()
    produto = {
            "nome": nome,
            "preco": preco,
            "qtd": qtd        
    }
    print(f"Nome: {nome}| Preço: {preco}Kz| Qtd: {qtd}, produto cadastrado com sucesso!")
    return produto


cadastrar()
