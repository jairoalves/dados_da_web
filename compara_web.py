# -*- coding: utf-8 -*-

# Acesso a dataset de UBS em funcionamento do site dados.gov.br
# http://dados.gov.br/dataset/mspainelsage_101

import requests 

def extrai_campos(registro):
#    Retorna nome, bairro, rua, cidade, estado do dado
    return registro['no_fantasia'], registro['no_bairro'], \
           registro['no_logradouro'], registro['cidade'], registro['uf']

def esp_horizontal(caractere='-', compr=40):
#    Espacamento horizontal
    linha = ''
    for cont in range(compr):
        linha = linha + caractere
    print (linha)

url = 'http://dados.gov.br/api/action/datastore_search'
cidade ='Remgio, PB' # Cidade desejada

params = dict(
    resource_id='9175f184-59a0-47a4-81f8-0d3c983b3a2d',
    q = cidade 
)

resp = requests.get(url=url, params=params)
dados = resp.json()['result']['records']

for registro in dados:
    nome, bairro, rua, cidade_lida, estado = extrai_campos(registro)
    
    esp_horizontal()
    print('Nome: ' + nome)
    print(rua.strip() + '.', 'Bairro:', bairro)
    print(cidade_lida + ',', estado + '.')
    
    
esp_horizontal()
print('Total =', resp.json()['result']['total'], 'Postos de Saude em', cidade)
