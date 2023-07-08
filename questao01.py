def constroiMatriz(tamanho):
    matriz = []
    for i in range(tamanho):
        list.append(matriz,[0]*tamanho)
    return matriz

def preencheMatriz(matriz, tamanho):
    for i in range(0, tamanho):
        for j in range(0, tamanho):
            while(True):
                try:
                    matriz[i][j] = int(input(f"Informe um número inteiro para a posição: [{i}][{j}]: "))
                    break
                except:
                    print("Valor inválido!")

def inverteDiagonaisMatriz(matriz, tamanho):
    aux = 0
    for i in range(0, tamanho):
        for j in range(0, tamanho):
            if (i == j):
                aux = matriz[i][j]
                matriz[i][j] = matriz[i][tamanho - 1 - j]
                matriz[i][tamanho - 1 - j] = aux

def imprimeMatriz(matriz, tamanho):
    for i in range(0, tamanho):
        for j in range(0, tamanho):
            print(f"[{matriz[i][j]:^3}]", end="")
        print()

if __name__ == '__main__':
    tamanho = int(input("Informe o tamanho da matriz: "))
    matriz = constroiMatriz(tamanho)

    preencheMatriz(matriz, tamanho)
    print("--------------------------Matriz-------------------------")
    imprimeMatriz(matriz, tamanho)

    inverteDiagonaisMatriz(matriz, tamanho)
    print("-----------Matriz coma as diagonais invertidas-----------")
    imprimeMatriz(matriz, tamanho)