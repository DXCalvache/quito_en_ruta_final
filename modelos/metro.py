from .transporte_publico import TransportePublico

class Metro(TransportePublico):
    def __init__(self, nombre, tarifa, capacidad, linea):
        super().__init__(nombre, tarifa, capacidad)
        self.linea = linea

    def mostrar_linea(self):
        print(f"Línea: {self.linea}")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        self.mostrar_linea()
