#intregação com o banco de dados ddo firebse (REST API)
import requests
import json

linkdb = 'https://fir-integration-ae3e9-default-rtdb.firebaseio.com'

#Criar uma venda (POST)

requisicao = requests.post(f'linkdb/produtos/.json')