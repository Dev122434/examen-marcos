class Areas():
    def __init__(self):
        self.base = 0
        self.altura = 0

    def leerDatos(self) -> None:
        self.base = float(input('Ingrese el valor de la base: '))
        self.altura = float(input('Ingrese el valor de la altura: '))

    def areaRectangulo(self) -> float:
        self.leerDatos()
        return self.base * self.altura

    def areaTriangulo(self):
        self.leerDatos()
        return (self.base * self.altura) / 2