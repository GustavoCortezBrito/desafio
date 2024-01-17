def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1 or numero == 2:
        return 1
    else:
        return (fibonacci(numero-1) + fibonacci(numero-2))


while True:
    numero_recebido = int(input("Qual o numero?"))

    if numero_recebido >= 0:
        print(fibonacci(numero_recebido))
    else:
        print("O número deve ser maior ou igual a 0")