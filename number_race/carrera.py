import random

# Solicitar la cantidad de jugadores y validar el rango
def obtener_cantidad_jugadores():
    while True:
        try:
            jugadores = int(input("Ingrese la cantidad de jugadores (2-4): "))
            if 2 <= jugadores <= 4:
                return jugadores
            else:
                print("Error: La cantidad de jugadores debe estar entre 2 y 4.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")

# Solicitar el nivel de dificultad del tablero y definir la meta
def seleccionar_nivel():
    niveles = {
        1: 20,
        2: 30,
        3: 50,
        4: 100
    }
    while True:
        try:
            print("Seleccione el nivel del tablero:")
            print("1. Nivel básico (20 posiciones)")
            print("2. Nivel intermedio (30 posiciones)")
            print("3. Nivel avanzado (50 posiciones)")
            print("4. Nivel experto (100 posiciones)")
            nivel = int(input("Ingrese el número del nivel (1-4): "))
            if nivel in niveles:
                return niveles[nivel]
            else:
                print("Error: Seleccione un nivel válido (1-4).")
        except ValueError:
            print("Error: Debe ingresar un número entero.")

# Función para lanzar los dados
def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

# Función principal del juego
def carrera_numerica():
    print("¡Bienvenido a la Carrera Numérica!")
    num_jugadores = obtener_cantidad_jugadores()
    meta = seleccionar_nivel()
    
    # Inicializar posiciones y contador de pares consecutivos
    posiciones = [0] * num_jugadores
    pares_consecutivos = [0] * num_jugadores
    
    ganador = None
    turno = 0

    while ganador is None:
        jugador_actual = turno % num_jugadores
        dado1, dado2 = lanzar_dados()
        movimiento = dado1 + dado2
        
        print(f"\nTurno del Jugador {jugador_actual + 1}:")
        print(f"Dado 1: {dado1}, Dado 2: {dado2} -> Avanza {movimiento} posiciones")
        
        # Actualizar la posición del jugador
        posiciones[jugador_actual] += movimiento
        
        # Revisar si el jugador ha ganado por llegar a la meta
        if posiciones[jugador_actual] >= meta:
            ganador = jugador_actual + 1
            print(f"¡El Jugador {ganador} ha llegado a la meta y es el ganador!")
            break
        
        # Comprobar si ha obtenido pares consecutivos
        if dado1 == dado2:
            pares_consecutivos[jugador_actual] += 1
            print(f"¡El Jugador {jugador_actual + 1} ha sacado un par consecutivo!")
            
            if pares_consecutivos[jugador_actual] == 3:
                ganador = jugador_actual + 1
                print(f"¡El Jugador {ganador} ha ganado por obtener tres pares consecutivos!")
                break
        else:
            pares_consecutivos[jugador_actual] = 0
        
        print(f"Posición actual del Jugador {jugador_actual + 1}: {posiciones[jugador_actual]}")
        
        # Avanzar al siguiente turno
        turno += 1

# Iniciar el juego
if __name__ == "__main__":
    carrera_numerica()
