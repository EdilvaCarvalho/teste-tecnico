import math

def quantidadeDeSubMatrizesDeUmaMatriz(linhaA, colunaA, linhaB, colunaB):
    linha = math.factorial(linhaA) / (math.factorial(linhaB) * math.factorial(linhaA - linhaB))
    coluna = math.factorial(colunaA) / (math.factorial(colunaB) * math.factorial(colunaA - colunaB))
    resultado = linha * coluna
    return resultado

if __name__ == '__main__':
    linhaA = int(input("Informe a quantidade de linhas de uma matriz A: "))
    colunaA = int(input("Informe a quantidade de colunas de uma matriz A: "))

    linhaB = int(input("Informe a quantidade de linhas de uma submatriz B: "))
    colunaB = int(input("Informe a quantidade de colunas de uma submatriz B: "))

    resultado = quantidadeDeSubMatrizesDeUmaMatriz(linhaA, colunaA, linhaB, colunaB)
    print(f"A quantidade de vezes que uma submatriz B pode ser encontrada na matriz A é {resultado}")
