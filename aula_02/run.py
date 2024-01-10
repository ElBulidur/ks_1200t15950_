
# Veriáveis
# Etrutura condicional
# Coleções (lista, dicionarios e tuplas)
# ESTRUTURA DE REPETIÇÃO


alunos = [
    {"Nome": "André", "Notas": (7,9,7.5,8)},
    {"Nome": "Ricardo", "Notas": (8.1,9,7.5,8)},
    {"Nome": "João", "Notas": (5,9,9,7.5)},
    {"Nome": "Luzia","Notas": (7,9,76.5,7)},
    {"Nome": "Angélica", "Notas": (9,5,7.5,8)},
]


# Quero imprimir os nomes dos alunos alinha verticalmente

# print(alunos[0]['Nome'])
# print(alunos[1]['Nome'])
# print(alunos[2]['Nome'])
# print(alunos[3]['Nome'])
# print(alunos[4]['Nome'])

# x = 0

# for aluno in alunos:
    # print(f"O nome do aluno é: {aluno['Nome']}")


# # for aluno in alunos:
#     print(f"O nome do aluno é: {aluno['Nome']}")
#     x = x + 1

#     if x == 3: break

alunos = [
    {"Nome": "André", "Notas": (7,9,7.5,8)},
    {"Nome": "Ricardo", "Notas": (8.1,9,7.5,8)},
    {"Nome": "João", "Notas": (5,9,9,7.5)},
    {"Nome": "Luzia","Notas": (7,9,76.5,7)},
    {"Nome": "Angélica", "Notas": (9,5,7.5,8)},
]

# for x in range(3): print(alunos[x]['Nome'])

# for x in range(3,7):
#     print(x)


# for i in range(3, len(alunos)):
#     print(alunos[i]['Nome'])


# for i in range(0, len(alunos)):  # len(alunos) => 5
#     print(alunos[i])


notas = {
    "1Bim": 9,
    "2Bim": 6,
    "3Bim": 8,
    "4Bim": 9,
}


for x in notas:
    pass
    # print(type(x))
    # print(x)
    # print(notas[x]) # notas['1Bim'] => 9
    # print(f"{x} esta com a nota {notas[x]}.")

# for chave in notas.keys():
#     print(chave)

# for valor in notas.values():
#     print(valor)


for bim, nota in notas.items():
    pass
    # print(f"{bim} esta com a nota {nota}.")


for letra in "julio":
    if letra == "l" or letra == "j" or letra == "o":
        letra = "*"

    # print(letra, flush=True, end="")


## While
        
x = 0 

while x <= 4:
    # print(x)
    x += 1


numero_par = 0

while numero_par == 0:
    num = int(input("Coloque um numero para: "))

    if num%2 == 0:
        numero_par = 1
    else:
        print("Errado tente de novo!")

