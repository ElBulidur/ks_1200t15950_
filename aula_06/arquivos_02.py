import os


arquivo = "notas_allunos.xlsx"

if os.path.exists(arquivo):
    print("Tem o arquivo!")

pasta = '../aula_051'

if os.path.isdir(pasta):
    print("Tem a pasta!")

# Saber a pasta que estar.
# print(os.getcwd())

# Navegar até uma pasta desejada!
# os.chdir("../aula_05")

# cria pasta
# os.mkdir("novos_arquivos")

# Deleta pasta 
# os.rmdir("novos_arquivos")
    
#Ler arquivos e diretorios na pasta atual
# dados = os.listdir()
# print(dados)

#Usar comando do terminal
# os.system("git status")


 ### CSV
import csv
    
alunos_novos = [
    ["Julio Pereira", "julio@email"],
    ["Fernando", "fernando@email"]
]

arquivo_csv = open("alunos_novos.csv", "w")

gravar = csv.writer(arquivo_csv, delimiter=",")
gravar.writerow(["Nome", "Email"])
gravar.writerows(alunos_novos)

arquivo_csv.close()

import openpyxl

pasta = openpyxl.load_workbook(filename="notas_alunos.xlsx")

alunos = []
for dados in pasta["boletim_incompleto"].iter_rows(values_only=True):
    if dados[0] and dados[0] != "aluno":
        alunos.append(dados[0])

print(alunos)


    


