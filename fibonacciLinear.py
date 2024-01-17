def fibonacci(numero):
    f1 = 1
    f2 = 1
    fn = 0
    if numero == 0:
        print(0)
    elif numero == 1 or numero == 2:
        print(1)
    else:
        for count in range(2, numero):
            fn = f1 + f2
            f2 = f1
            f1 = fn
            count += 1
        print(fn)



while True:
    numero_recebido = int(input("Qual o numero?"))

    if numero_recebido >= 0:
        fibonacci(numero_recebido)
    else:
        print("O número deve ser maior ou igual a 0")
