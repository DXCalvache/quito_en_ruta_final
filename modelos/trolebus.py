from .transporte_publico import TransportePublico

class Trolebus(TransportePublico):
    def __init__(self, nombre, tarifa, capacidad, corredor):
        super().__init__(nombre, tarifa, capacidad)
        self.corredor = corredor

    def mostrar_corredor(self):
        print(f"Corredor: {self.corredor}")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        self.mostrar_corredor()