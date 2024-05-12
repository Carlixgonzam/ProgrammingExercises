def diagonal_principal(matriz):
    # La función diagonal_principal toma 'matriz', que es una lista de listas.
    
    # La comprensión de lista [matriz[i][i] for i in range(len(matriz))] crea una lista de elementos
    # en la diagonal principal de la matriz.
    return [matriz[i][i] for i in range(len(matriz))]

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_principal(matriz))  # Salida: [1, 5, 9]