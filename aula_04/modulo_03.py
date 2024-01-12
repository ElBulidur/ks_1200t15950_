"""
    Laboratório 1

    Refazer o exercício relativo ao Caixa Eletrônico, considerando que o valor de cada cédula permanece armazenado
    em uma lista, ao invés de ser mostrado na tela.

"""

saque = valor = 135 #int(input("Digite o valor para saque(SOMENTE MULTIPLO DE 5): "))
cedulas = []

while saque%5 != 0:
    print("Este valor NÃO é multiplo de 5")
    saque = int(input("Tente novamente (SOMENTE MULTIPLO DE 5): "))


c50 = saque // 50
saque = saque % 50
cedulas.append(c50)

c20 = saque // 20
saque = saque % 20
cedulas.append(c20)

c10 = saque // 10 
saque = saque % 10 
cedulas.append(c10)

c5 = saque // 5 
cedulas.append(c5)
