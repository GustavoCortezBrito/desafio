def eh_numero_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            print(numero, "não é primo")
            return False
    print(numero, "é primo")
    return True


def encontrar_primos(numero):
    primos_lista = []
    for i in range(2, numero + 1):
        if eh_numero_primo(i):
            primos_lista.append(i)
    print(primos_lista)


while True:
    numero_recebido = int(input("Qual o numero?"))

    if numero_recebido > 1:
        encontrar_primos(numero_recebido)
    else:
        print("O número deve ser maior que 1")
