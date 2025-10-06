from clases.areas import Areas

def main():
    areas = Areas()
    #print(f'Area del rectangulo: {areas.areaRectangulo()}')
    #print(f'Area del triangulo: {areas.areaTriangulo()}')
    print(f'Area del circulo: {round(areas.areaCirculo(), 2)}')

main()