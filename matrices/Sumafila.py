def suma_fila(matriz, fila):
    # La función suma_fila toma dos parámetros: 'matriz', que es una lista de listas (matriz),
    # y 'fila', que es el índice de la fila cuyos elementos se sumarán.
    
    # La función sum() suma todos los elementos de la lista proporcionada.
    # matriz[fila] accede a la fila específica de la matriz.
    return sum(matriz[fila])

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(suma_fila(matriz, 1))  # Salida: 15
