def minimo_columna(matriz, columna):
    # La función minimo_columna toma dos parámetros: 'matriz', que es una lista de listas,
    # y 'columna', el índice de la columna de la que se busca el mínimo.
    
    # La comprensión de lista [fila[columna] for fila in matriz] crea una lista de todos los elementos en la columna especificada.
    # La función min() luego encuentra el valor mínimo de esa lista.
    return min(fila[columna] for fila in matriz)

matriz = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]
print(minimo_columna(matriz, 1))  # Salida: 0
