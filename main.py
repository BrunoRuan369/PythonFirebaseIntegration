#intregação com o banco de dados ddo firebse (REST API)
import requests
import json

linkdb = 'realtime database link'

#Criar uma venda (POST)

nome = input("Digite seu nome")
produto = input('qual produto voce comprou')
valor = input('preço do produto')

dados = {'cliente':nome,'produto':produto,'valor': valor }
requisicao = requests.post(f'{linkdb}/vendas/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

#Edita a venda (PATCH)

dados = {'cliente': 'Jose'}
requisicao = requests.patch(f'{linkdb}/vendas/-NKlTBV_FEzWDTEvjqot/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

#obter apenas uma venda ou todas as vendas (GET)

requisicao = requests.get(f'{linkdb}/.json')
print(requisicao)
print(requisicao.text)
