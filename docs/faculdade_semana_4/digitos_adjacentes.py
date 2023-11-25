def possui_adjacentes_iguais(numero):
  """Verifica se um número inteiro possui ao menos um dígito com um dígito adjacente igual a ele.

  Args:
    numero: O número inteiro a ser verificado.

  Returns:
    `True` se o número possui ao menos um dígito com um dígito adjacente igual a ele; `False` caso contrário.
  """

  numero_str = str(numero)
  for i in range(len(numero_str) - 1):
    if numero_str[i] == numero_str[i + 1]:
      return True
  return False


numero = int(input("Digite um número inteiro: "))

if possui_adjacentes_iguais(numero):
  print("sim")
else:
  print("não")
