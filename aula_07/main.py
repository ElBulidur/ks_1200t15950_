### MYSQL ###
import mysql.connector
import os

try: 
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="kasolution"
    )

    print("Conexão estabelecida com sucesso!")


except mysql.connector.Error as e:
    print(f"Erro encontrado: {e}")

# 244466666

def gerador_senha(senha):
    #Criar o seu script SQL
    sql = "INSERT INTO tb_senhas (senha) VALUES (%s)"

    #Pegar o cursor da conexão
    cursor = conn.cursor()

    #Exeecutar o script no banco através do cursor
    cursor.execute(sql, [senha])

    #comentar
    conn.commit()

    #Fechar conexão com bancos
    conn.close()

    return "Senha cadastrada com sucesso"

#CRUD ===> C=> CREATE, R => READ, U => UPDATE e D => DELETE <===


