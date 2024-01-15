"""
    Laboratório 1

    Escrever uma função que receba como parâmetro um número inteiro e retorne seu fatorial.

"""

# Imperial
def calcular_fatorial(num):
    fatorial = 1

    for x in range(num, 0, -1):
        fatorial = fatorial * x

    return fatorial

# print(calcular_fatorial(100))

"""
    Laboratório 2

    Escrever a mesma função do Laboratório anterior, mas desta vez usando recursividade.

"""
# Funcional

def calcular_fatorial_rec(num): #return 1 if num == 0 else num * calcular_fatorial_rec(num-1)

    if num == 0:
        return 1
    else:
        return num * calcular_fatorial_rec(num-1)
    
# print(calcular_fatorial_rec(10))

"""

    Laboratório 3

    Tomar como base o cálculo do Imposto de Renda Pessoa Física. O acesso para este cálculo pode ser realizado
    através do link: https://www27.receita.fazenda.gov.br/simulador-irpf/
    Escrever uma função que receba como parâmetro o valor da base de cálculo do salário, e retorne o imposto de
    renda correspondente.

    Sugestão: Usar tuplas para armazenar as faixas de valores.


"""

def calcular_irpf(salario):
    imposto = 0.0
    faixas = (0, 2112.00, 2826.65, 3751.06, 4664.68)
    aliquota = (0, 7.5, 15, 22.5, 27.5)
    base_calculo = salario - 528.00 #3472

    for i in range(4, -1, -1):
        if base_calculo > faixas[i]: #2
            imposto += (base_calculo - faixas[i]) * aliquota[i] / 100
            base_calculo = faixas[i]

    
    return imposto, base_calculo
    

imposto_devido = calcular_irpf(6000)

# print(f"O valor do imposto é {round(imposto_devido[0], 2)} porque o salario é maior do que {imposto_devido[1]}")



"""
    Laboratório 4

    Escrever uma função que receba como parâmetro uma lista variável de preços de produtos (itens de produtos)
    e uma lista de taxas aplicadas a estes produtos. A lista de produtos deve representar um parâmetro *args,
    enquanto a lista de taxas aplicadas, **kwargs.

"""


def calcular_produtos(*args, **kargs):
    soma = 0

    for valor in args:
        soma += valor
    
    taxa = 0
    imposto = 0

    valor_taxa = kargs.get("taxa")
    if valor_taxa:
        taxa = soma * valor_taxa

    valor_imposto = kargs.get("imposto")
    if valor_imposto:
        imposto = soma * valor_imposto

    return soma + taxa + imposto


# print(calcular_produtos(100, taxa=0.2, imposto=0.5))


