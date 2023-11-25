def gerador_numeros_impares(n):
  """
  Gera os n primeiros números ímpares naturais.

  Args:
    n: O número de números ímpares a gerar.

  Returns:
    Uma lista com os n primeiros números ímpares naturais.
  """

  impares = []
  for i in range(1, n + 1):
    impares.append(2 * i - 1)
  return impares


def main():
  """
  Programa principal.
  """

  n = int(input("Digite um número inteiro positivo: "))
  impares = gerador_numeros_impares(n)

  for impar in impares:
    print(impar)


if __name__ == "__main__":
  main()
