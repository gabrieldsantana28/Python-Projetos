# Exceção = é um objeto que represente um erro que ocorreu ao executar o programa
# Blocos try ... except

def div(k, j):
    return round(k/j,2)

if __name__ == "__main__":
    while True:
        try:
            n1 = int(input("Digite um número: "))
            n2 = int(input("Digite outro número: "))
            break
        except ValueError:
            print("Ocorreu um erro ao ler o valor, tente novamente.")
        try:
            r = div(n1,n2)
        except ZeroDivisionError:
            print(f"Não é possível dividir por zero!")
        except:
            ("Ocorreu um erro desconhecido...")

    try:
        r = round(n1/n2,2)
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
    else:
        print(f"Resultado: {r}")
    finally:
        print(f"Fim do cálculo.")

