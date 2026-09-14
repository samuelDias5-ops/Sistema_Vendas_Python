def pedir_numero(mensagem):
    while True:
        try:
            mensagem 
        except(TypeError,ValueError):
            print("Insira um valor válido!")
            continue
        else:
            break


#def pedir_qtd():
    #while True:
        #try:
         #   quantidade = int(input("Insira quantidade em estoque: "))
        #except(ValueError, TypeError):
          #  print("Insira um valor válido!")
         #   continue
        #else:
            #break
    
def cadastrar():
    nome = input("Insira o produto que deseja cadastrar: ").strip().lower()
    while True:
        #valor = float(input("Insira preço de produto:"))
        preco = pedir_numero("Insira preço do produto: ")
        #quantidade = int(input("Insira quantidade em estoque: "))
        qtd = pedir_numero("Insira quantidade em estoque: ")
        produto = {
                "nome": nome,
                "preco": preco,
                "qtd": qtd        
        }
        return produto


cadastrar()
