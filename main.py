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

def obtener_estado(tablero, jugador):
    """Obtiene una representación inmutable del estado del juego.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.
        jugador (str): Jugador al que le corresponde el turno.

    Returns:
        tuple: Configuración del tablero y jugador en turno.

    Raises:
        ValueError: Si el jugador no es "A" ni "B".
    """
    if jugador not in ("A", "B"):
        raise ValueError("El jugador debe ser 'A' o 'B'.")

    tablero_estado = tuple(tuple(fila) for fila in tablero)

    return tablero_estado, jugador
#TESST
#tablero = crear_tablero(5)
#estado_a = obtener_estado(tablero, "A")
#estado_b = obtener_estado(tablero, "B")
#print(estado_a == estado_b)

#Falta testear
def Mov_val(tablero, fila, columna, n):
    """Obtiene los movimientos válidos desde una posición del tablero.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.
        fila (int): Fila de origen.
        columna (int): Columna de origen.
        n (int): Tamaño del tablero.

    Returns:
        list[tuple[int, int]]: Coordenadas de destinos válidos.
    """
    mov = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i == 0 and j == 0:
                continue
            dist = max(abs(i), abs(j))
            if dist == 1 or dist == 2:
                nueva_fila = fila + i
                nueva_columna = columna + j
                if nueva_fila >= 0 and nueva_fila < n and nueva_columna >= 0 and nueva_columna < n:
                    if tablero[nueva_fila][nueva_columna] == ".":
                        mov.append((nueva_fila, nueva_columna))
    return mov
#tablero = crear_tablero(5)
#tablero[1][1] = "B"
#tablero[2][1] = "A"
#print(Mov_val(tablero, 0, 0, 5))

def Mov_ficha(tablero, fila, columna, nuevafila, nuevacolumna):
    """Realiza el movimiento de una ficha según su distancia.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.
        fila (int): Fila de origen.
        columna (int): Columna de origen.
        nuevafila (int): Fila de destino.
        nuevacolumna (int): Columna de destino.

    Returns:
        None: Modifica directamente el tablero.
    """
    i = abs(nuevafila - fila)
    j = abs(nuevacolumna - columna)

    dist = max(i, j)
    if dist == 2:
        tablero[nuevafila][nuevacolumna] = tablero[fila][columna]
        tablero[fila][columna] = "."

    elif dist == 1:
        tablero[nuevafila][nuevacolumna] = tablero[fila][columna]
#tablerin = crear_tablero(5)
#Mov_ficha(tablerin,0,0,2,2)
#print(tablerin)



def Capturar(tablero, fila, columna, jugador, n):
    """Convierte las fichas rivales adyacentes a la ficha jugada.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.
        fila (int): Fila de la ficha jugada.
        columna (int): Columna de la ficha jugada.
        jugador (str): Jugador que realizó el movimiento.
        n (int): Tamaño del tablero.

    Returns:
        None: Modifica directamente el tablero.
    """

    for i in range(-1, 2):
        for j in range(-1, 2):
            nueva_fila = fila + i
            nueva_columna = columna + j

            if nueva_fila >= 0 and nueva_fila < n and nueva_columna >= 0 and nueva_columna < n:
                if tablero[nueva_fila][nueva_columna] != "." and tablero[nueva_fila][nueva_columna] != jugador:
                    tablero[nueva_fila][nueva_columna] = jugador


#tobleron = crear_tablero(5)
#tobleron[2][1] = "B"
#tobleron[3][1] = "B"
#tobleron[3][2] = "B"
#tobleron[2][3] = "B"
#Capturar(tobleron, 2, 2, "A", 5)
#print(tobleron)