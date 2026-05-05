import random

# valor = random.randint(1,20)
# print(valor)

# print("Gerar cinco números aleatórios entre 1 e 50: \n")
# for i in range(5):
#     n = random.randint(1,50)
#     print(f"{i+1}º Número gerado: {n}")

# valor = random.random()
# print(f"Número gerado: {round(valor * 10, 2)}")

# valor = random.uniform(1,100)
# print(f"Número: {round(valor, 3)}")

l = [2,4,6,9,10,12,3,6,7,18,12,11]
# n = random.choice(l)
# print(f"Número escolhido: {n}")

# n = random.sample(l,4)
# print(f"Número escolhido: {n}")

# embaralhar
print(f"Exibir a lista original: {l}")
print(f"Embaralhar a lista: ", end="")
n = random.shuffle(l)
print(l)