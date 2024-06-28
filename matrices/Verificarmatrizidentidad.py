def es_identidad(matriz):
    # La función es_identidad toma 'matriz', que es una lista de listas.
    
    # La matriz es identidad si todos los elementos en la diagonal principal son 1
    # y todos los otros elementos son 0.
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
                return False
    return True

matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
print(es_identidad(matriz))  # Salida: True
