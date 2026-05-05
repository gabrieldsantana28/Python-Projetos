# Tuplas são imutáveis, não podem ser alteradas após criada

# tupla = (2,4,6,7,9)
# tupla[1] = 5 # Irá dar erro
# print(tupla)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr')
elementos = halogenios + gases_nobres
t1 = (5,2,6,8,4,5,9,2,1,0,12,22,14,4,18)
# print(halogenios[-3])
# print(t1.count(3))
# print(halogenios[1:3])
# print('Fe' in halogenios)
# print(sum(t1))

# Funções não disponíveis em tuplas: .sort(), .append(), .reverse(), .pop() - TUDO QUE ALTERA NÃO É DISPONÍVEL

# for elemento in elementos:
#     print(f"Elemento químico: {elemento}")

# grupo17 = list(halogenios)
# grupo17[0] = 'H'
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(type(grupo1))
print(type(alcalinos))

print(sorted(alcalinos)) # Funciona
print(alcalinos.sort()) # Não funciona
