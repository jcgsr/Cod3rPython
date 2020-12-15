# 11.11.2020

esta_chovendo = False

print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])
print('Hoje estou com as roupas '+('molhadas.' if esta_chovendo else 'secas'))

# OPERADOR DE MEMBRO
lista = [1, 2, 3, 4, "Ana"]
2 in lista
8 not in lista

# OPERADOR DE IDENTIDADE
x = 3
y = x
z = 3

x is y
y is z
x is not z
