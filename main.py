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

def imprimir_tablero(tablero):
    """Imprime el tablero con números de filas y columnas.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.

    Returns:
        None: La función únicamente imprime el tablero en pantalla.
    """
    for columna in range(1, len(tablero) + 1):
        print(columna, end=" ")
    print()

    for numero_fila, fila in enumerate(tablero, start=1):
        print(numero_fila, end=" ")

        for casilla in fila:
            print(casilla, end=" ")

        print()
#tablero_prueba = crear_tablero(5)
#imprimir_tablero(tablero_prueba)

def pedir_tamano_tablero():
    """Solicita y valida el tamaño del tablero de Attax.

    Returns:
        int: Tamaño válido del tablero, mayor o igual a 5.
    """
    while True:
        try:
            n = int(input("Ingrese tamaño del tablero: "))

            if n >= 5:
                return n
            else:
                print("N es menor que 5")

        except ValueError:
            print("Ingrese un numero entero")

#pedir_tamano_tablero()


def pedir_coordenadas(n):
    """Solicita y valida una coordenada de Attax.

    Args:
        n (int): Tamaño del tablero.

    Returns:
        tuple[int, int]: Fila y columna convertidas a índices desde 0.
    """
    while True:
        try:
            f = int(input("Ingrese fila: "))
            c = int(input("Ingrese columna: "))

            if f >= 1 and f <= n and c >= 1 and c <= n:
                return f - 1, c - 1
            else:
                print("Indices no validos")

        except ValueError:
            print("Ingrese un numero entero")

#pedir_coordenadas(4)

def pedir_jugada(n):
    """Solicita las coordenadas de origen y destino de una jugada.

    Args:
        n (int): Tamaño del tablero.

    Returns:
        tuple: Coordenadas de origen y destino de la jugada.
    """
    print("Ingrese coordenada de origen:")
    coordenada_origen = pedir_coordenadas(n)

    print("Ingrese coordenada de destino:")
    coordenada_destino = pedir_coordenadas(n)

    return coordenada_origen, coordenada_destino

#jugada_prueba = pedir_jugada(5)
#print(jugada_prueba)

def hay_triple_repeticion(historial, estado):
    """Registra un estado y comprueba si aparece por tercera vez.

    Args:
        historial (list): Estados registrados durante la partida.
        estado (tuple): Estado actual del tablero y jugador en turno.

    Returns:
        bool: True si el estado aparece al menos tres veces; False en caso contrario.
    """
    historial.append(estado)

    if historial.count(estado) >= 3:
        return True
    else:
        return False

#tablero = crear_tablero(5)
#historial = []
#estado_A = obtener_estado(tablero, jugador="A")
#print(hay_triple_repeticion(historial, estado_A))
#print(hay_triple_repeticion(historial, estado_A))
#estado_B = obtener_estado(tablero, jugador="B")
#print(hay_triple_repeticion(historial, estado_B))

def mostrar_resultado(tablero):
    """Muestra el resultado final de una partida de Attax.

    Args:
        tablero (list[list[str]]): Estado final del tablero.

    Returns:
        None: La función únicamente muestra el resultado en pantalla.
    """
    fichas_a, fichas_b = contar_fichas(tablero)
    ganador = obtener_ganador(tablero)
    if ganador == "A":
        print(f"El ganador es A con {fichas_a} fichas")
    elif ganador == "B":
        print(f"El ganador es B con {fichas_b} fichas")
    else:
        print(f"Empate con {fichas_a} fichas por jugador")

#tablero = crear_tablero(5)
#mostrar_resultado(tablero)