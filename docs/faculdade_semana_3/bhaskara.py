import math

# Input: Receive the coefficients a, b, and c of the quadratic equation
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the discriminant to determine the type of roots
if discriminant < 0:
    print("esta equação não possui raízes reais")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"a raiz desta equação é {root}")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    if root1 < root2:
        print(f"as raízes da equação são {root1} e {root2}")
    else:
        print(f"as raízes da equação são {root2} e {root1}")
