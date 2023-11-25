produtos = ["imac", "iphone", "celular"]

while True:
    novo_produto = input("Digite o nome do novo produto: ")
    novo_produto = novo_produto.lower()
    
    if "sair" == novo_produto:
        break
    
    if novo_produto in produtos:
        print("Produto já cadastrado")
    else:
        print(f"O item {novo_produto} está adicionado.")