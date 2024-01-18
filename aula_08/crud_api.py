import json, requests


### CRUD NA API DO MOCKAPI ####

#Create (POST)
def cadastrar_aluno(aluno):
    resposta = requests.post(url="https://65a8535f219bfa3718670926.mockapi.io/alunos", data=aluno)

    if resposta.status_code == 201:
        print("Aluno cadastrado com sucesso!")


# Read (GET)(1)
def pegar_nomes_alunos():
        
    resposta = requests.get(url="https://65a8535f219bfa3718670926.mockapi.io/alunos")

    if resposta.status_code == 200:
        conteudo = json.loads(resposta.content)

        alunos = []

        for aluno in conteudo:
            alunos.append(aluno)

        return alunos

# Read (GET)(2)
def pegar_aluno_pelo_id(id):
    resposta = requests.get(url=f"https://65a8535f219bfa3718670926.mockapi.io/alunos/{id}")

    if resposta.status_code == 200:
        conteudo = json.loads(resposta.content)  
        return conteudo


# Update (PUT)
def atualizar_media_e_status(id):
    aluno_atualidado = pegar_aluno_pelo_id(id)

    aluno_atualidado['media'] = (float(aluno_atualidado['bim1']) + float(aluno_atualidado['bim2'])  + float(aluno_atualidado['bim3'])  + float(aluno_atualidado['bim4']))/4

    if aluno_atualidado['media'] > 7:
        aluno_atualidado['status'] = "Aprovado"
    else:
        aluno_atualidado['status'] = "Reprovado"

    return aluno_atualidado

def atualizar_dados_do_aluno(dados, id):  

    resposta = requests.put(url=f"https://65a8535f219bfa3718670926.mockapi.io/alunos/{id}", data=dados)

    if resposta.status_code == 200:
        print("Aluno atualizado com sucesso!")


#Delete (DELETE)
def deletar_aluno():
    resposta = requests.delete(url=f"https://65a8535f219bfa3718670926.mockapi.io/alunos/{id}")

    if resposta.status_code == 200:
        nome = json.loads(resposta.content)['nome']
        print(f"O aluno {nome} foi deletado com sucesso!")


# alunos = pegar_nomes_alunos()

# print(alunos)

# for aluno in alunos:
#     atualizar_dados_do_aluno(atualizar_media_e_status(aluno['id']), aluno['id'])

# atualizar_dados_do_aluno(atualizar_media_e_status(14), 14)