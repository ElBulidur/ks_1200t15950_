

# funções


def menu_inicial():
    print("=== Calculador ===")
    print("")
    operador = input("Escolha uma operação (+, -, / ou *): ")
    num1 = float(input("Coloque o primeiro numero: "))
    num2 = float(input("coloque o segundo numero: "))

    return operador, num1, num2

def soma(a , b):
    print(f"A soma de {a} + {b} é: {a+b}")

    
def subtracao(a , b):
    print(f"A subtração de {a} - {b} é: {a-b}")


def divisao(a , b):
    print(f"A divisão de {a} - {b} é: {a/b}")


def multiplicao(a , b):
    print(f"A multiplicação de {a} * {b} é: {a*b}")




# opt = menu_inicial()

# # print(opt)

# if opt[0] == "+":
#     soma(opt[1], opt[2])
