
# main.py
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from datetime import datetime

# ========= funciones polimórficas =========
def sumar_areas(figuras: list):
    total = 0
    for f in figuras:
        total += f.area()
    return total


def sumar_perimetros(figuras: list):
    total = 0
    for f in figuras:
        total += f.perimetro()
    return total


# ========= PROGRAMA PRINCIPAL =========
print("=== Taller Figuras Geométricas ===")
print("Fecha y hora:", datetime.now())
print("-----------------------------------")

# Crear dos cuadrados y dos rectángulos
c1 = Cuadrado(5)
c2 = Cuadrado(10)

r1 = Rectangulo(4, 8)
r2 = Rectangulo(6, 3)

# Mostrar información
figuras = [c1, c2, r1, r2]

print("\n--- Impresión de objetos ---")
for fig in figuras:
    print(fig)
    print("Área:", fig.area())
    print("Perímetro:", fig.perimetro())
    print()

print("\n--- Prueba de encapsulamiento (valores inválidos) ---")
try:
    c1.ancho = -5
except ValueError as e:
    print("Error atrapado correctamente:", e)

print("\n--- Modificación de valores (válidos) ---")
r1.ancho = 20
r1.alto = 10
print("Nuevo rectángulo:", r1)
print("Nueva área:", r1.area())

print("\n--- Sumas Polimórficas ---")
print("Suma de áreas:", sumar_areas(figuras))
print("Suma de perímetros:", sumar_perimetros(figuras))
