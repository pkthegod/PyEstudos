number = int(input('Numero: '))

print('primo' if all(number % i for i in range(2, number)) else 'nao primo')
