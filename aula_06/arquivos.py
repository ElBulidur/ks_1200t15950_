### PERSISTENCIA ###

alunos = [
    "Dayane",
    "Jessica",
    "Roberto",
    "Julio"
]

# try:
#     int("inpy")

# except Exception as e:
#     log_file = open('logs.log', "w")
#     log_file.write(f"Erros encontrado\n")
#     log_file.write(f"{e}\n")
#     log_file.close()


# GRAVAR EM ARQUIVO
# Abrir o arquivo R = Read(Leitura) ou w = Writer (Gravação)
# arquivo_para_grava = open('alunos.txt', "w")

# arquivo_para_grava.write("Alunos\n")

# for aluno in alunos:
#     arquivo_para_grava.write(f"{aluno}\n")

# arquivo_para_grava.close()


#LER ARQUIVO

try: 
    arquivo_lido = open("alunos.txt", "r")

    # alunos = arquivo_lido.read(1)
    # aluno2 = arquivo_lido.read(2)
    aluno3 = arquivo_lido.readable()

    alunos_dict = {}

    # {Titulo: aluno, nome: Dayane}

    # print(aluno4)
    # print(type(alunos))

    # aluno4 = arquivo_lido.readlines()
    # for linha in aluno4:
    #     print(linha[0:-1])

    aluno = arquivo_lido.readline()[0:-1]
    aluno1 = arquivo_lido.readline()[0:-1]
    print(aluno)
    print(aluno1)


except FileNotFoundError:
    print("Não existe este arquivo. \
Verifica se você colocou o arquivo certo!")



