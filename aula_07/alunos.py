
import mysql.connector


# Cria a conexão
def conexao(host="localhost", user="root", password="root", database="kasolution"):
    try: 
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        return conn

    except mysql.connector.Error as e:
        print(f"Erro encontrado: {e}")

# Create
def criar_aluno(aluno):
    # Cria a conexão
    conn = conexao()

    # Criar o SQL
    sql = "INSERT INTO tb_alunos (nome, bim1, bim2, bim3, bim4, media, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    # Defenir o cursor
    cursor = conn.cursor()

    # Executar o SQL com o cursor
    cursor.execute(sql, aluno)

    # Comentar
    conn.commit()

    print(f"Aluno(a) {aluno[0]} criado com sucesso!")

    # Fecha a conexão
    conn.close()

#Read(1)
def pegar_alunos():
    conn = conexao()

    sql = "SELECT * FROM tb_alunos"

    cursor = conn.cursor()

    cursor.execute(sql)

    # cursor.fetchone() # Pegar a primeira linha do banco e retorna com tupla.
    # cursor.fetchmany() # pegar os valores como lista de tupla.

    alunos = []

    for linha in cursor:
        alunos.append(linha)

    conn.close()

    return alunos

#Read(2)
def pegar_aluno_pelo_id(id):

    conn = conexao()
    sql = "SELECT * FROM tb_alunos WHERE id=%s"

    cursor = conn.cursor()

    cursor.execute(sql, [id])

    registro = cursor.fetchone()

    conn.close()

    if registro:
        return registro
    else:
        return f"Não tem o aluno com id {id} no banco!"

def definir_nota_aluno(id):
    aluno = pegar_aluno_pelo_id(id)

    media = 0
    for nota in aluno[2:6]:
        media += nota

    media = round(media / len(aluno[2:6]),2)

    if media > 7 :
        status = "Aprovado"
    else:
        status = "Reprovado"

    return media, status, id

#Update
def atualizar_media_e_status(media, status, id):

    conn = conexao()

    sql = "UPDATE tb_alunos set media=%s, status=%s WHERE id=%s"

    cursor = conn.cursor()

    cursor.execute(sql, [media, status, id])

    if cursor.rowcount:
        conn.commit()
        conn.close()
        return f"Aluno do id {id} foi atualizado com sucesso!"
    else:
        conn.close()
        return f"Não existe no banco o aluno com id {id} ou já foi feito esta alteração."
    
#Delete
def deleta_aluno(id):

    conn = conexao()

    sql = "DELETE FROM tb_alunos WHERE id=%s"

    cursor = conn.cursor()

    cursor.execute(sql, [id])

    if cursor.rowcount:
        conn.commit()
        conn.close()
        return f"Aluno do id {id} foi deletado com sucesso!"
    else:
        conn.close()
        return f"Não existe no banco o aluno com id {id}."

aluno1 = ["Andréia Figueiredo", 7.5, 6.5, 7.9, 8.3, 0, ""]

#CREATE
# criar_aluno(aluno1)

#READ
# print(pegar_alunos()[0][1]) # Exemplo pegar o nome do aluno 01.
# print(pegar_aluno_pelo_id(5))

# UPDATE
# media, status, id = definir_nota_aluno(1)
# print( atualizar_media_e_status(media, status, id) )

#Delete
# print( deleta_aluno(2))

