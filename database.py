## Utilizando módulo ramdon
"""
import random

##print(dir(random))
##print(help(random.randint))
lista_items = ["Banana", "Pera", "laranja", "maracuja"]
print(random.randint(1,20))

print(random.choice(lista_items))
"""
import json
#print(dir(json))

produto = {
"id": 1,
"qtde": 3,
"nome": "Lactovacilos",
"unit_value": 34,
"price": 105
}

"""
f = open("base.json","w")
f.write("Mr White has too many faces")
f.close()
"""
def save_json(file_name,data):
    with open(file_name,"w") as write_file:
        json.dump(data,write_file)

def read_json(file_name):
    with open(file_name,"r") as read_file:
        return json.load(read_file)


"""
file = "base_homologacao.json"
compras = [produto,produto,produto,produto,produto]
save_json(file,compras)



resultado = read_json(file)
print(resultado)



print(r.read())
r.close()
"""
