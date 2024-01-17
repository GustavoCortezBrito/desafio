def eh_numero_primo_recursivo(numero, divisor=2):
    if numero == divisor:
        return True
    elif numero % divisor == 0:
        return False
    return eh_numero_primo_recursivo(numero, divisor + 1)

def encontrar_primos_recursivo(numero, atual=2):
    if atual <= numero:
        if eh_numero_primo_recursivo(atual):
            print(atual, end=" ")
        encontrar_primos_recursivo(numero, atual + 1)

while True:
    numero_recebido = int(input("Qual o numero?"))

    if numero_recebido > 1:
        encontrar_primos_recursivo(numero_recebido)
    else:
        print("O número deve ser maior que 1")
