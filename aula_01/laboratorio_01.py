"""
    Laboratório 1
        Escrever um programa em Python que solicite informações de três pessoas, como nome, idade, peso e altura.
        Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. Usar a formatação
        de interpolação.

"""

# nome1 = input("Escreva o nome da primeira pessoa: ")
# idade1 = input("Coloque a idade da primeira pessoa: ")
# peso1 = input("Coloque o peso da primeira pessoa: ")
# altura = input("Escreva a altura da primeira pessoa: ")


# print(f"PRIMEIRA PESSOA => \nNome: {nome1}, \nIdade: {idade1}, \npeso: {peso1}, \naltura: {altura}.")






"""
    Laboratório 2
        Suponha que em um caixa eletrônico existam cédulas disponíveis de 5, 10, 20 e 50 reais. Usando operações de
        divisão inteira e resto da divisão, escrever um programa que solicite ao usuário um valor para saque e, a partir
        deste valor, armazenar em variáveis e apresentar na tela a quantidade de cada cédula para compor o valor do
        saque.

        Obs.: Considerar neste exercício que os valores sejam sempre múltiplos de 5. Considerar também a menor
        quantidade possível de cédulas. 

"""

saque = valor = 135 #int(input("Digite o valor para saque(SOMENTE MULTIPLO DE 5): ")) # 135

if valor % 5 != 0:
    print("Este caixa aceita somento multiplos de 5")
else:

# 100 // 3 => 33
# 100 / 3 => 33.333333333336
# 100 % 3 => 1

    c50 = saque // 50 # 2
    saque = saque % 50 # 35

    c20 = saque // 20 # 1
    saque = saque % 20 # 15

    c10 = saque // 10 # 1
    saque = saque % 10 # 5

    c5 = saque // 5 # 1


    # print(f"Resultado: \nValor do saque: {valor} \n{c50} Cédula de 50,00\n{c20} Cédula de 20,00\n{c10} Cédulas de 10,00 \n{c5} Cédulas de 5,00")



## Operadores lógicos
    
n1 = 10
n2 = 20
n3 = 34

if not n1 == n2:  # Negação
    pass
    # print("Foi!!!")

if n1 == n2 or n1 != n3:  # Negação
    print("Foi!!!")