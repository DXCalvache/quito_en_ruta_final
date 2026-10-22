from .parada import Parada
# Una ruta agrupa paradas ya creadas con agregacion

class Ruta:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.paradas = []

    def agregar_parada(self, parada):
        if not isinstance(parada, Parada):
            raise TypeError("Se debe agregar un objeto Parada")
        self.paradas.append(parada)

    def mostrar_paradas(self):
        print(f"Ruta {self.codigo}: {self.nombre}")
        if not self.paradas:
            print("Sin paradas registradas")
        for parada in self.paradas:
            parada.mostrar_parada()