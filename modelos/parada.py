class Parada:
    def __init__(self, nombre, sector):
        self.nombre = nombre
        self.sector = sector

    def mostrar_parada(self):
        print(f"  - {self.nombre} ({self.sector})")