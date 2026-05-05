# num = 1

# while (num <= 10):
#     print(f"{num}º número")
#     num += 1
# print("Fim do laço!")

nome = None

while True:
    print("Digite seu nome, ou X para parar: ")
    nome = input()
    if nome == "X" or nome == "x":
        break
    print(f"Bem vindo, {nome}!")
print("Até logo!")