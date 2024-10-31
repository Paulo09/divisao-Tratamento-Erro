try:
    numerador = int(input("Digite o Numerador:"))
    denominador = int(input("Digite o Denominador:"))
    resultado = numerador/denominador
    print(f"O resultado da divisão é:{resultado}")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
except ValueError:
    print("Erro você deve digitar um número válido.")    