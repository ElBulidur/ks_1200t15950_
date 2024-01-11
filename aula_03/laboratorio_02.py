"""
    Laboratório 1

    Neste laboratório será refeito o exercício do Caixa Eletrônico, apresentado no laboratório do Módulo 1. A
    diferença é que aqui deverá ser verificado se o valor do saque é múltiplo de 5. Se não for, apresentar uma
    mensagem informado da impossibilidade de realização do saque.

"""

saque = valor = 10 #int(input("Digite o valor para saque(SOMENTE MULTIPLO DE 5): "))

while saque%5 != 0:
    print("Este valor NÃO é multiplo de 5")
    saque = int(input("Tente novamente (SOMENTE MULTIPLO DE 5): "))


c50 = saque // 50
saque = saque % 50

c20 = saque // 20
saque = saque % 20

c10 = saque // 10 
saque = saque % 10 

c5 = saque // 5 


# print(f"Resultado: \nValor do saque: {valor} \n{c50} Cédula de 50,00\n{c20} Cédula de 20,00\n{c10} Cédulas de 10,00 \n{c5} Cédulas de 5,00")





"""
    Laboratório 2

    Escrever um programa que solicite ao usuário:

        - O nome de um funcionário;
        - Seu salário.

    Se o salário for superior a R$ 5.000,00 ele terá um desconto de 10% sobre o que ultrapassar R$ 5.000,00.
    No final, apresentar:

        - O nome do funcionário;
        - O salário bruto;
        - O valor do desconto;
        - O salário líquido.
"""

funcionario = ""#input("Coloque o nome do funcionário: ")
salario = 0.0 #float(input("Salário Bruto: "))
desconto = 0


if salario > 5000:
    desconto = (salario - 5000) * 0.1

# print("")
# print("==== DADOS DO FUNCIONÁRIO ===")
# print(f"O nome do funcionário: {funcionario}")
# print(f"O salário bruto: {salario}")
# print(f"O valor do desconto: {round(desconto, 2)}")
# print(f"O salário líquido: {round(salario - desconto, 2)}")



"""
    Laboratório 3

    Em um clube, o valor da entrada varia de acordo com a idade do associado.
    Os critérios são:

        -  Até 17 anos - R$ 50,00;
        - Entre 18 e 59 anos - R$ 60,00;
        - A partir de 60 anos - R$ 20,00.

    O programa deve apresentar o nome do associado e o valor do ingresso a ser pago.
"""

try:
    nome_associado =input("Nome do associado: ")
    idade = int(input("Idade do associado: "))


    if idade <= 17:
        ingresso = 50
    elif idade >= 18 and idade <= 59:
        ingresso = 60
    else:
        ingresso = 20


    print(f"Nome do associado: {nome_associado}")
    print(f"Valor do ingresso: {ingresso}")
    
except TypeError as e:
    print(f"Erro de tipo")

except ValueError as e:
    print(f"Erro de Valor")