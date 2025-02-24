import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'

class Circulo:
    def __init__(self, centro=Punto(), radio=1.0):
        self.centro = centro
        self.radio = radio
    
    def __str__(self):
        return f'Circulo con centro en {self.centro} y radio {self.radio}'
    
    def dibuja_circulo(self):
        fig, ax = plt.subplots()
        circulo = plt.Circle((self.centro.x, self.centro.y), self.radio, fill=False, edgecolor='b')
        ax.add_patch(circulo)
        ax.set_xlim(self.centro.x - self.radio - 1, self.centro.x + self.radio + 1)
        ax.set_ylim(self.centro.y - self.radio - 1, self.centro.y + self.radio + 1)
        ax.set_aspect('equal')
        plt.grid()
        plt.show()

c = Circulo(Punto(2, 3), 5)
print(c)
c.dibuja_circulo()
