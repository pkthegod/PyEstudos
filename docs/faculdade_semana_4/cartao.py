meuCartao = int(input("Digite o numero do seu cartão de credito: "))

cartaoLido = 1
encontreiMeuCartao = False

while cartaoLido != 0 and not encontreiMeuCartao:
    cartaoLido = int(input("Digite o numero do proximo cartão: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartao = True
        
if encontreiMeuCartao:
    print("Meu cartão tá lá")
else:
    print("Putz, meu cartão não tá lá")