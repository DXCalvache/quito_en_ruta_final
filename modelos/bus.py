from .transporte_publico import TransportePublico

class Bus(TransportePublico):
    def __init__(self, nombre, tarifa, capacidad, cooperativa):
        super().__init__(nombre, tarifa, capacidad)
        self.cooperativa = cooperativa

    def mostrar_cooperativa(self):
        print(f"Cooperativa: {self.cooperativa}")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        self.mostrar_cooperativa()
