# figura_geometrica.py

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    # ======= GETTERS =======
    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    # ======= SETTERS =======
    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

    # ======= MÉTODOS =======
    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    def __str__(self):
        return f"FiguraGeometrica(ancho={self.ancho}, alto={self.alto})"
