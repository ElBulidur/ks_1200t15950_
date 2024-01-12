"""    
    Laboratório 1

        Criar um programa que utilize uma estrutura de repetição for. Nesta estrutura, o usuário deverá fornecer 5 nomes
        a serem adicionados em uma lista. No final, apresentar os nomes em ordem crescente.

"""

# nomes = []

# for x in range(5):
#     nome = input(f"Coloque o {x+1}° nome: ")
#     nomes.append(nome)

# nomes.sort()

# print(nomes)

######### Segunda meio de solução ####################

# nomes = [input(f"Coloque o {x+1}° nome: ") for x in range(5)]
# nomes.sort()
# print(nomes)

#######



"""
    Laboratório 2

        Neste laboratório, uma lista de 100 números será criada de forma aleatória, ou seja, os elementos serão números
        aleatórios.
        Escrever o programa de forma a exibir E adicionar em uma lista, apenas os valores gerados que sejam maiores que
        10.

"""
import random as rn


# numeros = [] 
# repeticoes = {}

# for x in range(100):
#     numero =  rn.randint(0,15)

#     if numero > 10:
#         print(numero)
#         numeros.append(numero)


# for num in numeros: repeticoes[num] = numeros.count(num)

# print(f"Foram gerados {len(numeros)} numeros.")
# print(f"Valores e vezes que foram repetidos: {repeticoes}") 


"""
    Laboratório 3

    Escrever um programa que produza uma senha com 4 dígitos numéricos onde cada dígito é um valor aleatório
    entre 0 e 9.
    A senha resultante deve ser uma string.
    Observação: cada dígito gerado deve ser concatenado com o próximo.

"""

# senha = ''

# for x in range(4): 
#     numero = str(rn.randint(0,9))
#     senha += numero
    
# print(f"Senha gerada pelo sistema: {senha}")

"""
    Laboratório 4

    Neste laboratório, o usuário fornece as informações: dia, mês e ano.
    Com base nestas informações, determinar quantos dias restam para terminar o ano informado.
    Realizar as validações:

    - O mês informado deve estar na faixa entre 1 e 12;
    - O dia informado deve ser compatível com o mês informado;
    - Usar o ano para determinar o número de dias do mês de fevereiro.
"""

# dia = int(input("Coloque o dia a do mes: "))
# mes = int(input("Coloque o mes: "))
# ano = int(input("Coloque o ano: "))

# if mes < 1 or mes > 12:
#     raise ValueError("Tem que ser um numero de 1 a 12.")

# meses = (31, 29 if ano%4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# if dia < 1 or dia > meses[mes-1]:
#     raise ValueError("Dia fora do mês informado.")


# dias_restantes = meses[mes-1] - dia

# for x in range(mes, 12): 
#     dias_restantes += meses[x]

# print(f"Faltam {dias_restantes}.")






"""
    Laboratório 5

    Neste laboratório, o usuário fornece uma certa quantidade de números. O programa termina quando o usuário
    informar o número 0.

    Se o número informado for negativo, este será ignorado (só conta os números positivos). Em seguida, apresentar
    a soma e a quantidade de números informados.

    Observação: fazer uso dos comandos break e continue.
"""

# soma = 0
# quantidade = 0


# while True:
#     numero = int(input("Informe o numero: "))

#     if numero == 0:
#         break

#     if numero < 0:
#         continue

#     soma += numero
#     quantidade += 1

# print(f"A soma dos numero foram: {soma}")
# print(f"A quantidade dos numeros foram: {quantidade}")


"""
    Laboratório 6

    Este programa representa um jogo para adivinhar números. Os passos são apresentados a seguir, com um
    exemplo de uso:

        - O programa produz um número aleatório inteiro entre 1 e 100 (suponha: 49);
        - O programa pede para o usuário: "Informe um valor entre 0 e 100": 60;
        - Como o número informado é maior que o produzido, o programa pede: "Informe um valor entre 0 e 59"
        : 20;
        - Como o número informado é menor que o produzido, o programa pede: "Informe um valor entre 21 e
        59";
        - No final, o programa apresenta o número de tentativas.

    Observação: se o usuário fornece um valor fora da faixa solicitada, conta como tentativa.
"""

numero_sorteado = rn.randint(1,100)
tentativas = 0
minimo = 0
maximo = 100

while True:
    tentativas += 1
    numero = int(input(f"Informe um número entre {minimo} e {maximo}: "))

    if numero < minimo or numero > maximo:
        continue

    if numero > numero_sorteado:
        maximo = numero - 1

    elif numero < numero_sorteado:
        minimo = numero + 1
    else:
        break


print(f"Você acertou em {tentativas} Tentativas.")

    

    




