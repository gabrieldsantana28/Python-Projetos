bebidas = []

for i in range(5):
    bebida = input(f"Digite o nome da {i + 1}ª bebida: ")
    bebidas.append(bebida)

bebidas_ordenadas = sorted(bebidas)
bebidas.sort()
print("\nLista de bebidas cadastradas:")
for bebida in bebidas:
    print(bebida)
