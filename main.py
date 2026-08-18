def crear_tablero(n):
    """Creacion de la configuracion inicial de un tablero para Attax

    args:
        n (int): Tamaño del tablero. Debe ser mayor o igual a 5.

    returns:
        list[list[str]]: Matriz de n x n con la configuracion inicial

    Raises:
        ValueError: Si n es menor que 5
    """
    if n < 5:
        raise ValueError("El tamaño del tablero debe ser mayor o igual a 5")

    tablero = [["."for _ in range(n)] for _ in range(n)]

    tablero[0][0] = "A"
    tablero[n-1][n-1] = "A"

    tablero[0][n-1] = "B"
    tablero[n-1][0] = "B"

    return tablero

#tablero = crear_tablero(5)
#for fila in tablero:
    #print(fila)

def contar_fichas(tablero):
    fichas_a = 0
    fichas_b = 0
    for fila in tablero:
        for casila in fila:
            if casila == "A":
                fichas_a += 1
            elif casila == "B":
                fichas_b += 1
    return fichas_b, fichas_a

#tablero = crear_tablero(5)
#fichas_a, fichas_b = contar_fichas(tablero)

#print(fichas_a, fichas_b)

def tablero_lleno(tablero):
    for fila in tablero:
        if "." in fila:
            return False

    return True

    
#PRUEBA ARTIFICIAL
#tablero_prueba = [
    ["A", "A", "B", "A", "B"],
    ["B", "A", "B", "A", "B"],
    ["A", "B", "A", "B", "A"],
    ["B", "A", "B", "A", "B"],
    ["A", "B", "A", "B", "A"]
#]

#print("¿Tablero lleno?:", tablero_lleno(tablero_prueba))