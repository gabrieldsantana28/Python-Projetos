# Simples, composto ou encadeado

n1 = n2 = media = 0.0

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1+n2) / 2

if (media >= 7):
    print("Aprovado!")
elif (media < 10) or (media < 0):
    print("Erro.")
else:
    print("Reprovado")
print("Sua média é {}".format(media))
