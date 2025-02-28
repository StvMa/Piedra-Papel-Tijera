import random

# Variables globales para estadísticas
historial_partidas = []  # Lista que almacenará el historial de todas las partidas jugadas
estadisticas = {}  # Diccionario que llevará las estadísticas de cada jugador (ganadas, perdidas, empatadas)

# Función del menú principal que ejecuta el juego
def menu_principal(): 
    while True:
        # Mostrar opciones del menú
        print("\n--- Piedra Papel Y Tijeras ---")
        print("1. Jugar")
        print("2. Reglas del juego")
        print("3. Salir del juego")
        
        # Obtener la opción del usuario
        opcion = input("Elige una opción (1/2/3): ")
        
        # Ejecutar acciones dependiendo de la opción seleccionada
        if opcion == "1":
            jugar()  # Llama a la función para jugar
        elif opcion == "2":
            mostrar_reglas()  # Muestra las reglas del juego
        elif opcion == "3":
            print("Ok, Hasta luego.")  # Salir del juego
            break
        else:
            print("Opción no válida. Intenta de nuevo.")  # Si la opción no es válida, pide nuevamente

# Función que muestra las reglas del juego
def mostrar_reglas():
    print("\n>>> Reglas del Juego <<<")
    print("1. Cada jugador elige entre Piedra, Papel o Tijeras.")
    print("2. Piedra vence a Tijeras, Tijeras vence a Papel, Papel vence a Piedra.")
    print("3. Si ambos jugadores eligen lo mismo, es un empate.")
    print("4. En el modo multijugador, ambos jugadores eligen en secreto antes de revelar sus elecciones.")

# Función que permite jugar, con opciones para jugar contra la computadora o multijugador
def jugar():
    global historial_partidas, estadisticas
    historial_partidas = []  # Limpiar historial de partidas
    estadisticas.clear()  # Limpiar estadísticas previas
    
    while True:
        # Mostrar opciones para jugar
        print("\n--- Menú de Juego ---")
        print("1. Jugar contra la computadora")
        print("2. Multijugador (2 jugadores)")
        print("3. Ver estadísticas de la última partida")
        print("4. Regresar al menú principal")
        
        # Obtener la opción del usuario
        opcion = input("Elige una opción (1/2/3/4): ")
        
        # Ejecutar acciones dependiendo de la opción seleccionada
        if opcion == "1":
            jugar_vs_cpu()  # Jugar contra la computadora
        elif opcion == "2":
            jugar_dos_jugadores()  # Jugar con otra persona
        elif opcion == "3":
            mostrar_estadisticas()  # Ver estadísticas
        elif opcion == "4":
            break  # Regresar al menú principal
        else:
            print("Opción no válida. Intenta de nuevo.")  # Opción no válida

# Función para jugar contra la computadora
def jugar_vs_cpu():
    nombre_jugador = input("Ingresa tu nombre: ")  # Pedir nombre del jugador
    estadisticas[nombre_jugador] = {"ganadas": 0, "perdidas": 0, "empatadas": 0}  # Inicializar estadísticas del jugador
    estadisticas["Computadora"] = {"ganadas": 0, "perdidas": 0, "empatadas": 0}  # Inicializar estadísticas de la computadora
    rondas = definir_rondas()  # Definir número de rondas a jugar
    opciones = ["Piedra", "Papel", "Tijeras"]  # Opciones del juego
    
    for _ in range(rondas):
        # Pedir la elección del jugador
        jugador = input(f"{nombre_jugador}, elige (Piedra/Papel/Tijeras): ").capitalize()
        if jugador not in opciones:
            print("Elección no válida. Intenta de nuevo.")
            continue
        
        # La computadora elige aleatoriamente
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")
        
        # Determinar quién ganó y actualizar estadísticas
        determinar_ganador(nombre_jugador, "Computadora", jugador, computadora)
    
    mostrar_estadisticas()  # Mostrar estadísticas después de todas las rondas

# Función para jugar en modo multijugador (2 jugadores)
def jugar_dos_jugadores():
    nombre1 = input("Nombre del primer jugador: ")  # Pedir nombre del primer jugador
    nombre2 = input("Nombre del segundo jugador: ")  # Pedir nombre del segundo jugador
    estadisticas[nombre1] = {"ganadas": 0, "perdidas": 0, "empatadas": 0}  # Inicializar estadísticas del jugador 1
    estadisticas[nombre2] = {"ganadas": 0, "perdidas": 0, "empatadas": 0}  # Inicializar estadísticas del jugador 2
    rondas = definir_rondas()  # Definir número de rondas a jugar
    opciones = ["Piedra", "Papel", "Tijeras"]  # Opciones del juego
    
    for _ in range(rondas):
        # Pedir elección del jugador 1 en secreto
        jugador1 = input(f"{nombre1}, elige en secreto (Piedra/Papel/Tijeras): ").capitalize()
        print("\n" * 50)  # Limpiar pantalla para ocultar la elección
        # Pedir elección del jugador 2 en secreto
        jugador2 = input(f"{nombre2}, elige en secreto (Piedra/Papel/Tijeras): ").capitalize()
        print("\n" * 50)  # Limpiar pantalla para ocultar la elección
        
        if jugador1 not in opciones or jugador2 not in opciones:
            print("Uno de los jugadores ingresó una opción no válida. Intenta de nuevo.")
            continue
        
        # Determinar quién ganó y actualizar estadísticas
        determinar_ganador(nombre1, nombre2, jugador1, jugador2)
    
    mostrar_estadisticas()  # Mostrar estadísticas después de todas las rondas

# Función para definir el número de rondas a jugar
def definir_rondas():
    opcion = input("¿Deseas definir un número de rondas? (Sí/No): ").lower()
    if opcion == "sí" or opcion == "si":
        try:
            return int(input("Ingrese el número de rondas a jugar: "))
        except ValueError:
            print("Entrada no válida. Se jugará una sola ronda por defecto.")
            return 1
    return 1  # Si no se define, jugará solo una ronda

# Función para determinar el ganador de una ronda
def determinar_ganador(jugador1, jugador2, eleccion1, eleccion2):
    global historial_partidas, estadisticas
    
    # Mostrar las elecciones de ambos jugadores
    print(f"{jugador1} eligió: {eleccion1}")
    print(f"{jugador2} eligió: {eleccion2}")
    
    # Determinar el resultado de la partida
    if eleccion1 == eleccion2:
        resultado = "Empate"
        estadisticas[jugador1]["empatadas"] += 1  # Actualizar empate para jugador 1
        estadisticas[jugador2]["empatadas"] += 1  # Actualizar empate para jugador 2
    elif (eleccion1 == "Piedra" and eleccion2 == "Tijeras") or \
         (eleccion1 == "Papel" and eleccion2 == "Piedra") or \
         (eleccion1 == "Tijeras" and eleccion2 == "Papel"):
        resultado = f"{jugador1} ganó"
        estadisticas[jugador1]["ganadas"] += 1  # Actualizar victoria para jugador 1
        estadisticas[jugador2]["perdidas"] += 1  # Actualizar derrota para jugador 2
    else:
        resultado = f"{jugador2} ganó"
        estadisticas[jugador2]["ganadas"] += 1  # Actualizar victoria para jugador 2
        estadisticas[jugador1]["perdidas"] += 1  # Actualizar derrota para jugador 1
    
    # Agregar el resultado al historial de partidas
    historial_partidas.append(f"{jugador1}: {eleccion1} - {jugador2}: {eleccion2} - Resultado: {resultado}")

# Función que muestra el historial y estadísticas de todas las partidas jugadas
def mostrar_estadisticas():
    if not historial_partidas:
        print("No hay estadísticas recientes.")
        return
    
    # Mostrar historial de todas las partidas jugadas
    print("\n>>>> Histórico de Partidas <<<<")
    for partida in historial_partidas:
        print(partida)
    
    # Mostrar estadísticas de victorias, derrotas y empates por jugador
    print("\n>>>> Estadísticas <<<<")
    for jugador, datos in estadisticas.items():
        print(f"{jugador}: {datos['ganadas']} ganadas, {datos['perdidas']} perdidas, {datos['empatadas']} empatadas")

# Llamada a la función principal para ejecutar el juego
menu_principal()
