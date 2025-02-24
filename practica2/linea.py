import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2
    
    def __str__(self):
        return f"Línea desde {self.p1} hasta {self.p2}"
    
    def dibuja_linea(self):
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], marker='o')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Dibujo de Línea")
        plt.grid()
        plt.show()

punto1 = Punto(0, 0)
punto2 = Punto(5, 5)
linea = Linea(punto1, punto2)
print(linea)
linea.dibuja_linea()
