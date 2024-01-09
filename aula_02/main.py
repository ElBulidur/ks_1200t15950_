
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


print(type(aluno))
print(aluno)









