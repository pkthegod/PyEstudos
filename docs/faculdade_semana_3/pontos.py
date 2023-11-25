# Input: Receive four numbers, representing (x1, y1) and (x2, y2)
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

# Calculate the distance using the distance formula
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Check the condition and print the result
if distance >= 10:
    print("longe")
else:
    print("perto")
