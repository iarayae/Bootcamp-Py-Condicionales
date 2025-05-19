# Código según lo solicitado en Desafío


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