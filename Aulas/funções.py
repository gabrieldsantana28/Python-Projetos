# Funções
# Modularização, Reúso de Código, Legibilidade

# def <nome_funcao> ([argumentos]):
#     <instrucoes>

# def mensagem():
#     print('Bóson Treinamentos em Tecnologia')
#     print('Curso Completo de Python')
    
# mensagem()

# Função com argumentos
# def soma(a,b):
#     c = a+b
#     print(f"A soma dos números é igual a: {c}")

# soma(12,7)

def mult(x,y):
    return x * y

# a = 5
# b = 8
# c = mult(a,b)
# print(f"O produto de {a} e {b} é {c}")

def div(k,j):
    if j != 0:
        return k/j
    else:
        return "Impossível dividir por 0"

# if __name__ == '__main__':
#     a = int(input("Digite um número: "))
#     b = int(input("Digite um número: "))

#     r = div(a,b)
#     print(f'{a} dividido por {b} é igual a {r}')

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2,5,7,3,4,8]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)