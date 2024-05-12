def contar_ceros(matriz):
    # La función contar_ceros toma 'matriz', que es una lista de listas.
    
    # Se utiliza sum() en una comprensión de lista con una condición interna
    # que cuenta 1 para cada cero encontrado en la matriz.
    return sum(1 for fila in matriz for elemento in fila if elemento == 0)

matriz = [
    [1, 0, 3],
    [0, 5, 6],
    [7, 0, 0]
]
print(contar_ceros(matriz))  # Salida: 4