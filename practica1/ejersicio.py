import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x**2 + self.y**2)
        angulo = math.atan2(self.y, self.x)  
        return radio, angulo

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Punto(2, 3)


x, y = p1.coord_cartesianas()
print("Coordenadas Cartesianas:", x, y)


r, a = p1.coord_polares()
print("Coordenadas Polares:", r, a)
