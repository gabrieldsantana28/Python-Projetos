# Set
planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)
print(len(planeta_anao))

# for astro in planeta_anao:
#     print(astro.upper(), end=" ")

# astros = ['Lua', 'Vênus', 'Sírius', 'Marte', 'Lua']
# print(astros, end=" ")
# astros_set = set(astros)
# print(astros_set)

astros1 = {'Lua', 'Vênus', 'Sírius', 'Marte', 'Lua'}
astros2 = {'Lua', 'Vênus', 'Sírius', 'Marte', 'Lua', 'Cometa de Halley'}
# print(astros1 != astros2)

# União dos conjuntos
# print(astros1 | astros2)
# print(astros1.union(astros2))

# # Semelhança dos conjuntos
# print(astros1 & astros2)
# print(astros1.intersection(astros2))

# # Diferença dos conjuntos
# print(astros1 ^ astros2)
# print(astros1.symmetric_difference(astros2))

astros1.add('Urano')
astros1.add('Sol')
print(astros1)
astros1.remove('Sol')
astros1.pop()
# astros1.clear
print(astros1)