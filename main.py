def crear_tablero(n):
    """Crea la configuración inicial de un tablero para Attax.

    Args:
        n (int): Tamaño del tablero. Debe ser mayor o igual a 5.

    Returns:
        list[list[str]]: Matriz de n x n con la configuración inicial.

    Raises:
        ValueError: Si n es menor que 5.
    """
    if n < 5:
        raise ValueError("El tamaño del tablero debe ser mayor o igual a 5")

    tablero = [["." for _ in range(n)] for _ in range(n)]

    tablero[0][0] = "A"
    tablero[n - 1][n - 1] = "A"
    tablero[0][n - 1] = "B"
    tablero[n - 1][0] = "B"

    return tablero


def contar_fichas(tablero):
    """Cuenta las fichas de ambos jugadores en el tablero.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.

    Returns:
        tuple[int, int]: Cantidad de fichas de A y B, respectivamente.
    """
    fichas_a = 0
    fichas_b = 0

    for fila in tablero:
        for casilla in fila:
            if casilla == "A":
                fichas_a += 1
            elif casilla == "B":
                fichas_b += 1

    return fichas_a, fichas_b


def tablero_lleno(tablero):
    """Comprueba si el tablero no contiene casillas vacías.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.

    Returns:
        bool: True si el tablero está lleno; False en caso contrario.
    """
    for fila in tablero:
        if "." in fila:
            return False

    return True


def jugador_sin_fichas(tablero, jugador):
    """Comprueba si un jugador se quedó sin fichas.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.
        jugador (str): Jugador que se desea comprobar.

    Returns:
        bool: True si el jugador no tiene fichas; False en caso contrario.

    Raises:
        ValueError: Si el jugador no es "A" ni "B".
    """
    fichas_a, fichas_b = contar_fichas(tablero)

    if jugador == "A":
        return fichas_a == 0
    if jugador == "B":
        return fichas_b == 0

    raise ValueError("El jugador debe ser 'A' o 'B'.")


def cambiar_turno(jugador):
    """Cambia el turno entre los jugadores A y B.

    Args:
        jugador (str): Jugador actual.

    Returns:
        str: Jugador al que corresponde el siguiente turno.

    Raises:
        ValueError: Si el jugador no es "A" ni "B".
    """
    if jugador == "A":
        return "B"
    if jugador == "B":
        return "A"

    raise ValueError("El jugador debe ser 'A' o 'B'.")


def obtener_ganador(tablero):
    """Obtiene al jugador con mayor cantidad de fichas.

    Args:
        tablero (list[list[str]]): Estado final del tablero.

    Returns:
        str | None: "A" o "B" si existe ganador; None si hay empate.
    """
    fichas_a, fichas_b = contar_fichas(tablero)

    if fichas_a > fichas_b:
        return "A"
    if fichas_a < fichas_b:
        return "B"

    return None


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

            print("N es menor que 5")

        except ValueError:
            print("Ingrese un numero entero")


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

            if 1 <= f <= n and 1 <= c <= n:
                return f - 1, c - 1

            print("Indices no validos")

        except ValueError:
            print("Ingrese un numero entero")


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


def hay_triple_repeticion(historial, estado):
    """Registra un estado y comprueba si aparece por tercera vez.

    Args:
        historial (list): Estados registrados durante la partida.
        estado (tuple): Estado actual del tablero y jugador en turno.

    Returns:
        bool: True si el estado aparece al menos tres veces.
    """
    historial.append(estado)
    return historial.count(estado) >= 3


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

                dentro_filas = 0 <= nueva_fila < n
                dentro_columnas = 0 <= nueva_columna < n

                if (
                    dentro_filas
                    and dentro_columnas
                    and tablero[nueva_fila][nueva_columna] == "."
                ):
                    mov.append((nueva_fila, nueva_columna))

    return mov


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

            dentro_filas = 0 <= nueva_fila < n
            dentro_columnas = 0 <= nueva_columna < n

            if dentro_filas and dentro_columnas:
                casilla = tablero[nueva_fila][nueva_columna]

                if casilla != "." and casilla != jugador:
                    tablero[nueva_fila][nueva_columna] = jugador


def tiene_movimientos(tablero, jugador, n):
    """Comprueba si un jugador tiene al menos un movimiento válido.

    Args:
        tablero (list[list[str]]): Estado actual del tablero.
        jugador (str): Jugador cuyas fichas se revisarán.
        n (int): Tamaño del tablero.

    Returns:
        bool: True si el jugador tiene al menos un movimiento válido;
        False en caso contrario.
    """
    for fila in range(n):
        for columna in range(n):
            if tablero[fila][columna] == jugador:
                movimientos = Mov_val(tablero, fila, columna, n)

                if movimientos:
                    return True

    return False


def juego_ataxx():
    """Ejecuta una partida completa de Attax entre dos jugadores humanos.

    Gestiona los turnos, la validación de movimientos, clonaciones,
    saltos, capturas y las condiciones de término de la partida,
    incluyendo tablero lleno, jugador sin fichas, turnos consecutivos
    sin movimientos y triple repetición.

    Returns:
        None: La función ejecuta la partida mediante entrada y salida
        por consola.
    """
    n = pedir_tamano_tablero()
    tablero = crear_tablero(n)
    jugador = "A"
    historial = []
    turnos_sin_movimiento = 0
    empate_repeticion = False

    estado_inicial = obtener_estado(tablero, jugador)
    historial.append(estado_inicial)

    while True:
        imprimir_tablero(tablero)

        if tablero_lleno(tablero):
            break

        print(f"Turno del jugador {jugador}")

        if not tiene_movimientos(tablero, jugador, n):
            print(
                f"El jugador {jugador} no tiene movimientos. "
                "Pasa su turno."
            )
            turnos_sin_movimiento += 1

            if turnos_sin_movimiento == 2:
                break

            jugador = cambiar_turno(jugador)
            estado = obtener_estado(tablero, jugador)

            if hay_triple_repeticion(historial, estado):
                empate_repeticion = True
                break

            continue

        turnos_sin_movimiento = 0

        while True:
            print("Ingrese coordenada de origen:")
            fila, columna = pedir_coordenadas(n)

            if tablero[fila][columna] == jugador:
                movimientos = Mov_val(tablero, fila, columna, n)

                if movimientos:
                    break

                print("Esa ficha no tiene movimientos disponibles")
            else:
                print("Debes seleccionar una ficha propia")

        while True:
            print("Ingrese coordenada de destino:")
            nueva_fila, nueva_columna = pedir_coordenadas(n)

            if (nueva_fila, nueva_columna) in movimientos:
                break

            print("Destino no válido")

        Mov_ficha(tablero, fila, columna, nueva_fila, nueva_columna)
        Capturar(tablero, nueva_fila, nueva_columna, jugador, n)

        rival = cambiar_turno(jugador)

        if tablero_lleno(tablero) or jugador_sin_fichas(tablero, rival):
            break

        jugador = cambiar_turno(jugador)
        estado = obtener_estado(tablero, jugador)

        if hay_triple_repeticion(historial, estado):
            empate_repeticion = True
            break

    imprimir_tablero(tablero)

    if empate_repeticion:
        print("Empate por triple repetición")
    else:
        mostrar_resultado(tablero)

juego_ataxx()