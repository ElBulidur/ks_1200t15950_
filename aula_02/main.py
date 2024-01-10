
## VARIÁVEIS
## OPERADORES
## ESTRUTURA CONDICIONAL

## Analizar o aluno com sua media geral:
# Se tiver abaixo de 7 está Reprovado
# Se tiver entre 7 e 8 esta em Recuperação
# Se tiver a partir de 8 esta Aprovado.

# media_geral = float(input("Coloque a média geral do aluno: "))

#  APROVADO / REPROVADO
# if media_geral > 7.9:
#     print("Aluno Aprovado!")
# else:
#     print("Aluno Reprovado!")


#  APROVADO / REPROVADO / RECUPERAÇÃO
# if media_geral < 7: print("Aluno Reprovado!")
# elif media_geral < 8: print("Aluno em !")
# else: print("Aluno Aprovado!")


#  APROVADO / REPROVADO
# print("Aluno Aprovado!") if media_geral > 6.9 else print("Aluno Reprovado!")


# if media_geral > 6.9:
#     pass
#     # print("Aluno Aprovado!")
# else:
#     pass


# COLEÇÕES (MUTÁVEL OU IMUTÁVEL)

# LISTAS => MUTÁVEL

aluno = ["Gabriel", 22, 87, 1.78, True] #list

# print(type(aluno)) #Tipo
# print(aluno)
# print(aluno[0])
# aluno[0] = "Fernando"
# print(aluno[0])
# print(aluno[-1]) # Pegando o último elemento
# aluno[0] = 39
# print(aluno[0])

# print(len(aluno)) # Verificar o tamanho da list

## METÓDOS (RETORNAR INFORMAÇÃO OU NÃO)
numeros = [1,4,6,7,9,10]

# numeros.append(60) #Adicionar elemento no final da lista (Não)

# numeros.clear() # Limpar a lista (Não)


# retorna = numeros.copy() # Cria uma cópia (Retorna a cópia)

# retorna = numeros.count(7) # Retorna a quantidade repetida (Retorna a quantidade)

# numeros.sort() # Ordena os valores

# retorna = numeros.pop(1) # Retira o elemento de acordo com a posição.

# numeros.remove(9) # Remove o elemento através do valor


# DICIONÁRIO (MUTÁVEL)


aluno = {
    "nome": "Roberto", 
    "Idade": 18, 
    "Peso": 80, 
    "Altura": 1.78, 
    "Aprovado": True
} #Dict



# print(type(aluno))
# print(aluno)

# print(aluno['nome'])
# print(aluno.get('nome')) # Retorna None se não encontrar a chaves.

# retorna = aluno.keys() # Retorna as chaves
# retorna = aluno.values() # retorna os calores
# retorna = aluno.items() # retorna os os items

aluno['nome'] = "Julio"



# TUPLAS (IMUTÁVEL)

numeros = (1,"Julio") # tuple

# print(type(numeros))
# print(numeros)


# retorna = numeros.count(1)
# retorna = numeros.index(1) # Retorna a posição do elemento

dias_da_semana = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom")


# LISTAS, DICIONÁRIOS E TUPLAS

alunos = [
    {"Nome": "André", "Notas": (7,9,7.5,8)},
    {"Nome": "Ricardo", "Notas": (8.1,9,7.5,8)},
    {"Nome": "João", "Notas": (5,9,9,7.5)},
    {"Nome": "Luzia","Notas": (7,9,76.5,7)},
    {"Nome": "Angélica", "Notas": (9,5,7.5,8)},
]


# print(" === Notas alunos ===")

# print(f"Nome: {alunos[0]['Nome']}, \
#       1 Bim: {alunos[0]['Notas'][0]}, \
#         2 Bim: {alunos[0]['Notas'][1]}, \
#             3 Bim: {alunos[0]['Notas'][2]} e \
#                 4 Bim: {alunos[0]['Notas'][3]}")

id_usuarios = ["Julio", "Andréia", "Gilberto"]

amizades_julio = (1,2)

amizades = [
    (0,1),
    (0,2),
    (2,1)
]


print(alunos[0].items())








