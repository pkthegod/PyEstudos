def fatorial(n):
  """
  Calcula o fatorial de um número natural n.

  Args:
    n: O número natural a ser calculado.

  Returns:
    O fatorial de n.
  """

  if n == 0:
    return 1
  else:
    return n * fatorial(n - 1)


def main():
  """
  Programa principal.
  """

  n = int(input("Digite um número natural: "))
  print(fatorial(n))


if __name__ == "__main__":
  main()
