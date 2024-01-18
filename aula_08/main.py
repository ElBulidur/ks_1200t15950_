import json, requests

cep = 35024410

resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json")


if resposta.status_code == 200:
    print(f"Código de resposta com sucesso: {resposta.status_code}")

# print(resposta.content)

conteudo = json.loads(resposta.content)

# print(conteudo)

print(f"Meu endereço: {conteudo['logradouro']} - {conteudo['bairro']}")