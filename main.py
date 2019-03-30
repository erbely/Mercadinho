"""

Projeto para mercadinho e controle de estoque

Requirements for our Market

We want our staff to be able to browse the PRODUCTS in the INVENTORY
We also want the ability to SELL products to customers
We want to be able to buy products we are lower at.
Every product has a buying price and selling price.
We want to get a report of our sells, inventory and profit margin
We want to have an alert for items lower than 5 in INVENTORY

INVENTORY = "Database with PRODUCTS"
PRODUCTS = "Dictionary with ID, name, unit value and quantity"
FINANCE = "Stores the sells"

Dictionary = { "key": "value", "key2": "value2", "key3": 123}
print(Dictionary["key2"]) #value2

List = ["Banana", "maca", "laranja", "jaca"]
print(List[-1])

print(produto2["nome"])

print(estoque[2]["nome"])

tuple = ("item1", "item2", 123, dictionary, array, list)

# add_estoque(produto1)
# add_estoque(produto2)
# add_estoque(produto3)


variavel1, variavel2, variavel3 = "banana", "laranja", 123

produto1 = {
"id": 0,
"qtde":1,
"nome": "bolacha traquinas",
"unit_value": 2
 }

produto2 = {
"id": 1,
"qtde": 2,
"nome": "Sabão Ace",
"unit_value": 4
 }

produto3 = {
"id": 2,
"qtde": 5,
"nome": "cerveja bavaria",
"unit_value": 3.5
}

"""
import database
import os

banco = "estoque.json"

if os.path.isfile(banco):
    # Load Database
    estoque = database.read_json(banco)
else:
    # Starting our estoque empty
    estoque = [] # Incialiação de lista vazia, uma vez que não há BD

def add_estoque(x):
    print("Produto {} adicionado com sucesso!".format(x["nome"]))
    estoque.append(x)

def verifica_se_produto_existe(nome_do_produto): # Tang
    # Verificar se produto já existe, caso exista, somar quantidade
    resposta = "s"
    id = 0
    for index, prod in enumerate(estoque):
        if nome_do_produto in prod["nome"]:
            resposta = input("Produto {} existente. Adicionar NOVO produto?[s/n]".format(nome_do_produto))
            id = index

    if resposta.lower() == "s":
    #    print(resposta, id)
        return True, id
    else:
    #    print(resposta, id)
        return False, id

#TODO criar função adicionar_quantidade
#TODO criar Lista histórico_de_compra a partir de unit_value para gerar média das últimas 3 compras para gerar preço_de_venda - Data, valor, quantidade, fornecedor
#TODO criar função preço_de_venda - verifica se o campo price eh igual a 0, e usa a formula nesse campo.
#TODO criar front end flask
#TODO criar em docker
#TODO Banco de dados em JSON - OK

def adicionar_quantidade():
    pass

def preco_de_venda(porcentagem):
    print("adicionando {}% aos produtos".format(porcentagem))
    lucro_bruto = 0
    for value in estoque:
        aumento = value["unit_value"] * (porcentagem / 100)
        lucro_bruto += aumento
        # print(f'valor do aumento {aumento}')
        # print('valor do aumento {}'.format(aumento))
        value["price"] = value["unit_value"] + aumento
    return lucro_bruto

def add_produto(nova_qtde, nome, unit_value):
    resposta, id_para_somar = verifica_se_produto_existe(nome)
    # estou recebendo (True, id)
    # resposta = verifica_se_produto_existe(nome)[0]
    # id_para_somar = verifica_se_produto_existe(nome)[1]
    #print(resposta, id_para_somar)
    if resposta:
        idnext = len(estoque)
        produto = {
        "id": idnext,
        "qtde": nova_qtde,
        "nome": nome,
        "unit_value": unit_value,
        "price": 0
        }
        add_estoque(produto)
    else:
    #    print("id recebido {}".format(id_para_somar))
        estoque[id_para_somar]["qtde"] += nova_qtde
        print(estoque[id_para_somar]["qtde"])
        print("Quantidade {} adicionada ao produto {}".format(nova_qtde, estoque[id_para_somar]["nome"]))

"""
add_produto(3, "bolacha traquinas", 2)
add_produto(5, "cerveja Itaipava", 1.70)
add_produto(7, "Jamelão", 4.50)
add_produto(3, "ração para minhoca", 4.00)
add_produto(55, "dinheiro de brinquedo", 1.00)
add_produto(20, "bala juquinha", 0.10)
add_produto(15, "Manga Gala", 0.80)
add_produto(7, "Super Massa Grow", 5.50)
"""
def consulta_estoque():
    for value in estoque:
        print("Nome: {} quantidade: {} valor de compra: {}  valor de venda: {} total gasto: {}".format(value["nome"],value["qtde"],value["unit_value"],value["price"],value["qtde"] * value["unit_value"]))
    print("Lucro Bruto: {}".format(lucro_bruto))


database.save_json(banco,estoque)

lucro_bruto = preco_de_venda(45)

consulta_estoque()

# print("Itens no estoque: {} {} {}".format(estoque[0]["nome"],estoque[0]["qtde"],estoque[0]["unit_value"]))
"""
Powered by Raphiluccio!

"""
