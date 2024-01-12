

# def nome_função(lista_parametros):
#   bloco_da_função


# Função sem parametro e sem retorno
def imprimir_ola_mundo():
    print("Olá mundo!")

#executar função
# imprimir_ola_mundo()
    
# Função com parametro, mas sem retorno
def imprimir_boas_vindas(cliente):
    print(f"Seja bem vindo(a), {cliente}.")

# imprimir_boas_vindas("Julio Pereira")
    
#Função sem parametro, mas com retorno
def retorna_numero_aleatorio():
    from random import random as rd

    return rd()

numero_aleatorio = retorna_numero_aleatorio()
# print(numero_aleatorio)

#Função com parametro e com retorno
def retorna_nome_completo(nome, sobrenome):
    return f"{nome} {sobrenome}"


nome_completo = retorna_nome_completo("julio", "jereira")
# print(nome_completo)


# Função com inferencia
def retorna_nome_maiusculo(nome: str):
    return nome.upper()


nome_maiusculo = retorna_nome_maiusculo("julio")
# print(nome_maiusculo)


#Função com parametros infinitos (args)
def somar_descontos(*args):
    total_descontos = 0

    for desconto in args:
        total_descontos = total_descontos + desconto
    
    return total_descontos


total_descontos = somar_descontos(1, 2, 2)
# print(total_descontos)

#Função com keys infinita
def somar_impostos(**kargs):

    if kargs.get("inss"):
        return kargs

impostos = somar_impostos(dpvat=100, fgts=240, inss=23)
# print(impostos)

def verificar_erros_tipos(valor):
    if type(valor) == str:
        return True
    
    return None

entrada = input("coloca apenas numero: ")

if verificar_erros_tipos(entrada):
    print("houve um erro no sistema!")

def verifica_entrada(entrada):
    try:
        int(entrada)
    except:
        return True
    
    return None

entrada = input("coloca apenas numero: ")

if verifica_entrada(entrada):
    print("houve um erro no sistema!")