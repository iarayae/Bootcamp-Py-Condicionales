# Código con paso adicional para volver a jugar (extra)


# Carga de módulos Sys y Random
import sys
import random

# Verificación de los argumentos ingresados
if len(sys.argv) != 2:
    print("Uso: python cachipun.py <piedra|papel|tijera>")
    sys.exit(1)

# Captura del argumento
jugador = sys.argv[1].lower()

# Validación del argumento
opciones = ["piedra", "papel", "tijera"]
if jugador not in opciones:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    sys.exit(1)

while True:
    # Jugada del Computador (random)
    computador = random.choice(opciones)

    # Mostrar jugadas
    print(f"Tu jugaste {jugador}.")
    print(f"Computador jugó {computador}.")

    # Combinaciones de Jugadas
    if jugador == computador:
        print("Empate.")
    elif (
        (jugador == "piedra" and computador == "tijera") or
        (jugador == "tijera" and computador == "papel") or
        (jugador == "papel" and computador == "piedra")
    ):
        print("Jugador ha ganado.")
    else:
        print("Jugador ha perdido.")
    
    # Extra: Pregunta para volver a jugar
    while True:
        jugar_nuevamente = input("¿Deseas jugar otra vez? (Si/No): ").lower()
        if jugar_nuevamente == "si":
            jugador = input("Ingresa tu jugada (piedra, papel o tijera): ").lower()
            if jugador not in opciones:
                print("Argumento inválido: Debe ser piedra, papel o tijera.")
                sys.exit(1)
            break
        elif jugar_nuevamente == "no":
            print("Gracias por jugar.")
            sys.exit(0)
        else:
            print("Respuesta no válida. Por favor escribe 'si' o 'no'.")

