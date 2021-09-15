# Calculadora usando laço de repetição

while True:
    print()
    sair = input('Deseja sair?: [s]im ou [n]ão: ')
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o Operador ( + - / * ): ')


    if sair == 's':
        break


    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um número. ')
        continue
    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador invalido!')