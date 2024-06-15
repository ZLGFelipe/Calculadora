print("Nome: Felipe Z. Lacerda Guedes RA: 195239\n")

executar = True

while executar:

    num1 = int(input("Escolha um numero: "))

    num2 = int(input("Escolha outro numero: "))

    operacao = ""

    while operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/":
        operacao = input("Qual operação deseja fazer? (+, -, *, /) ")

    if operacao == "+":
        print(f"A soma de {num1} + {num2} = {num1 + num2}")

    elif operacao == "-":
        print(f"A diferença de {num1} - {num2} = {num1 - num2}")

    elif operacao == "*":
        print(f"A multiplicação de {num1} * {num2} = {num1 * num2}")

    elif operacao == "/":
        if num2 != 0:
            print(f"O quociente de {num1} / {num2} = {num1 / num2}")
        else:
            print("O denominador não póde ser 0.")

    continuar = ""
    while continuar != "y" and continuar != "n":
       continuar = input("Deseja continuar calculando? (y/n) ").lower()
    
    if continuar == "n":
        print("Obrigado, espero te ver novamente.")
        executar = False
