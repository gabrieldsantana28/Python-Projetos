# Escopo Global e Local
var_global = "Curso Completo de Python"

def escreve_texto():
    global var_global
    var_global = "Banco de Dados com SQL"
    var_local = "Gabriel Santana"
    print(f"Variável Global: {var_global}")
    print(f"Variável Local: {var_local}")

if __name__ == "__main__":
    print(f"Ececutar a função escreve_texto()")
    escreve_texto()

    print("Tenta acessar as variáveis diretamente")
    print(f"Vairável Global: {var_global}")
    # print(var_local) # Acontece erro, pois é uma variável local = só pode ser usada dentro da função onde foi criada