
# REGRAS DA PROGRAMACAO FUNCIONAL
# TODAS AS SUAS FUNCOES TEM QUE INDEPENDENTES:
    # as funcoes precisa de no minimo um argunmento
    # as funcoes precisam retornar algo
    # as funções não podem ter loops(FOR, WHILE)


# imperial
num1 = 10
num2 = 20

def soma():
    return num1 + num2

# funcional
def soma(num1, num2):
    return num1 + num2

# ==========================

letra = "j"

# print(letra.upper())

# função anonima (lambda)

letra_maiuscula = lambda letra: letra.upper()

# print(letra_maiuscula("l"))


def soma_dois_numeros(num1, num2):
    if type(num1) != int or type(num2) != int:
        return "Não pode ser feito o calculo."
    
    return num1 + num2


soma_dois_lambda = lambda x, y: soma_dois_numeros(x, y)


resposta = soma_dois_lambda("10", 20)

# print(resposta)

# ======================
nome = "julio"

letras_em_maiusculo = []

for l in nome:
    letras_em_maiusculo.append(l.upper())

# print(letras_em_maiusculo)
    
letra_maiuscula = lambda x: x.upper()

letra = list(map(letra_maiuscula, nome)) #[]


# print(letra)

## MAP
numeros = [1, 2, 3, 4, 5]

resultado = list( map(lambda x: x+1 , numeros) )


print(resultado)





