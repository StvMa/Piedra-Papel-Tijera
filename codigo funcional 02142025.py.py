import random

# Variables globales para estadísticas
historial_partidas = []
estadisticas = {}

#En esta función se define el menú principal, incluyendo el término clave "while true".

def menu_principal(): 
    while True:
        print("\n--- Piedra Papel Y Tijeras ---")
        print("1. Jugar")
        print("2. Reglas del juego")
        print("3. Salir del juego")
        opcion = input("Elige una opción (1/2/3): ")
        
        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_reglas()
        elif opcion == "3":
            print("Ok, Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

#En esta función se define el apartado de "Reglas del juego".

def mostrar_reglas():
    print("\n>>> Reglas del Juego <<<")
    print("1. Cada jugador elige entre Piedra, Papel o Tijeras.")
    print("2. Piedra vence a Tijeras, Tijeras vence a Papel, Papel vence a Piedra.")
    print("3. Si ambos jugadores eligen lo mismo, es un empate.")
    print("4. En el modo multijugador, ambos jugadores eligen en secreto antes de revelar sus elecciones.")

#En esta función se define el apartado "jugar" y se llama a la variable global, para mostrar las estadísticas de rondas.

def jugar():
    global historial_partidas, estadisticas
    historial_partidas = []
    estadisticas.clear()
    
    while True:
        print("\n--- Menú de Juego ---")
        print("1. Jugar contra la computadora")
        print("2. Multijugador (2 jugadores)")
        print("3. Ver estadísticas de la última partida")
        print("4. Regresar al menú principal")
        opcion = input("Elige una opción (1/2/3/4): ")
        
        if opcion == "1":
            jugar_vs_cpu()
        elif opcion == "2":
            jugar_dos_jugadores()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

#En este apartado dentro de jugar, se definen funciones como, "jugar contra la computadora" y "Multijugador". incluyendo variables como ("jugador1" y "jugador2"), para los nombres.

def jugar_vs_cpu():
    nombre_jugador = input("Ingresa tu nombre: ")
    estadisticas[nombre_jugador] = {"ganadas": 0, "perdidas": 0, "empatadas": 0}
    estadisticas["Computadora"] = {"ganadas": 0, "perdidas": 0, "empatadas": 0}
    rondas = definir_rondas()
    opciones = ["Piedra", "Papel", "Tijeras"]
    
    for _ in range(rondas):
        jugador = input(f"{nombre_jugador}, elige (Piedra/Papel/Tijeras): ").capitalize()
        if jugador not in opciones:
            print("Elección no válida. Intenta de nuevo.")
            continue
        
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")
        determinar_ganador(nombre_jugador, "Computadora", jugador, computadora)
    
    mostrar_estadisticas()

def jugar_dos_jugadores():
    nombre1 = input("Nombre del primer jugador: ")
    nombre2 = input("Nombre del segundo jugador: ")
    estadisticas[nombre1] = {"ganadas": 0, "perdidas": 0, "empatadas": 0}
    estadisticas[nombre2] = {"ganadas": 0, "perdidas": 0, "empatadas": 0}
    rondas = definir_rondas()
    opciones = ["Piedra", "Papel", "Tijeras"]
    
    for _ in range(rondas):
        jugador1 = input(f"{nombre1}, elige en secreto (Piedra/Papel/Tijeras): ").capitalize()
        print("\n" * 50)  # Oculta la elección
        jugador2 = input(f"{nombre2}, elige en secreto (Piedra/Papel/Tijeras): ").capitalize()
        print("\n" * 50)  # Oculta la elección
        
        if jugador1 not in opciones or jugador2 not in opciones:
            print("Uno de los jugadores ingresó una opción no válida. Intenta de nuevo.")
            continue
        
        determinar_ganador(nombre1, nombre2, jugador1, jugador2)
    
    mostrar_estadisticas()

#En este apartado se define la función para elegir las rondas a jugar.

def definir_rondas():
    opcion = input("¿Deseas definir un número de rondas? (Sí/No): ").lower()
    if opcion == "sí" or opcion == "si":
        try:
            return int(input("Ingrese el número de rondas a jugar: "))
        except ValueError:
            print("Entrada no válida. Se jugará una sola ronda por defecto.")
            return 1
    return 1

def determinar_ganador(jugador1, jugador2, eleccion1, eleccion2):
    global historial_partidas, estadisticas
    
    print(f"{jugador1} eligió: {eleccion1}")
    print(f"{jugador2} eligió: {eleccion2}")
    
    if eleccion1 == eleccion2:
        resultado = "Empate"
        estadisticas[jugador1]["empatadas"] += 1
        estadisticas[jugador2]["empatadas"] += 1
    elif (eleccion1 == "Piedra" and eleccion2 == "Tijeras") or \
         (eleccion1 == "Papel" and eleccion2 == "Piedra") or \
         (eleccion1 == "Tijeras" and eleccion2 == "Papel"):
        resultado = f"{jugador1} ganó"
        estadisticas[jugador1]["ganadas"] += 1
        estadisticas[jugador2]["perdidas"] += 1
    else:
        resultado = f"{jugador2} ganó"
        estadisticas[jugador2]["ganadas"] += 1
        estadisticas[jugador1]["perdidas"] += 1
    
    historial_partidas.append(f"{jugador1}: {eleccion1} - {jugador2}: {eleccion2} - Resultado: {resultado}")

#En esta funcion se define el mostrar estadisticas.

def mostrar_estadisticas():
    if not historial_partidas:
        print("No hay estadísticas recientes.")
        return
    
    print("\n>>>> Histórico de Partidas <<<<")
    for partida in historial_partidas:
        print(partida)
    
    print("\n>>>> Estadísticas <<<<")
    for jugador, datos in estadisticas.items():
        print(f"{jugador}: {datos['ganadas']} ganadas, {datos['perdidas']} perdidas, {datos['empatadas']} empatadas")

# llamado a la funcion del menú
menu_principal()
