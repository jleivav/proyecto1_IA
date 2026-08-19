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
    return fichas_a, fichas_b

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

def jugador_sin_fichas(tablero, jugador):
    fichas_a, fichas_b = contar_fichas(tablero)

    if jugador == "A":
        return fichas_a == 0
    elif jugador == "B":
        return fichas_b == 0
    else:
        raise ValueError("El jugador debe ser 'A' o 'B'.")

tablero = crear_tablero(5)
#print("¿A esta sin fichas?:", jugador_sin_fichas(tablero, "A"))


#PRUEBA ARTIFICIAL
#tablero[0][4] = "."
#tablero[4][0] = "."
#print("¿B esta sin fichas?:", jugador_sin_fichas(tablero, "B"))

def cambiar_turno(jugador):
    if jugador == "A":
        return "B"
    elif jugador == "B":
        return "A"
    else:
        raise ValueError("El jugador debe ser 'A' o 'B'.")
#TESTING
#jugador = "A"
#print(jugador)
#jugador = cambiar_turno(jugador)
#print(jugador)
#jugador = cambiar_turno(jugador)
#print(jugador)

def obtener_ganador(tablero):
    fichas_a, fichas_b = contar_fichas(tablero)
    if fichas_a > fichas_b:
        return "A"
    elif fichas_a < fichas_b:
        return "B"
    else:
        return None
#CASO NONE
#tablero = crear_tablero(5)
#print("ganador:", obtener_ganador(tablero))

#CASO A
#tablero[1][1] = "A"
#print("Ganador:", obtener_ganador(tablero))

#CASO B
#tablero[1][1] = "B"
#print("Ganador:", obtener_ganador(tablero))