import math
from FigurasGeometricas import FiguraGeometrica

class Circumference(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self._radio = valor

    def area(self):
        return math.pi * self.radio * self.radio

    def perimeter(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circumference de radio: {self.radio}"