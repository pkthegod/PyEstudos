def soma_digitos(numero):
  """
  Calcula a soma dos dígitos de um número inteiro.

  Args:
    numero: O número inteiro a ser calculado.

  Returns:
    A soma dos dígitos do número.
  """

  soma = 0
  while numero > 0:
    resto = numero % 10
    soma += resto
    numero //= 10
  return soma


def main():
  """
  Programa principal.
  """

  numero = int(input("Digite um número inteiro: "))
  soma = soma_digitos(numero)
  print(soma)


if __name__ == "__main__":
  main()
