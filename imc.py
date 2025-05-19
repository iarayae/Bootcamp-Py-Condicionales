# Código según lo solicitado en Desafío


# Carga de módulo Sys
import sys

# Verificación de los argumentos ingresados
if len(sys.argv) != 3:
    print("Uso: python imc.py <peso_kg> <altura_cm>")
    sys.exit(1)

# Captura de los argumentos
peso_kg = float(sys.argv[1])
altura_cm = float(sys.argv[2])

# Conversión de argumentos y cálculo IMC
altura_m = altura_cm/100
imc = peso_kg / (altura_m ** 2)

# Resultado
print(f"Su IMC es {imc:.2f}")

# Clasificación IMC por OMS
if imc < 18.5:
    print("La clasificación OMS es Bajo Peso")
elif imc < 25:
    print("La clasificación OMS es Adecuado")
elif imc < 30:
    print("La clasificación OMS es Sobrepeso")
elif imc < 35:
    print("La clasificación OMS es Obesidad Grado I")
elif imc < 40:
    print("La clasificación OMS es Obesidad Grado II")
else:
    print("La clasificación OMS es Obesidad Grado III")