# Clase padre
from .ruta import Ruta
class TransportePublico:
    def __init__(self, nombre, tarifa, capacidad):
        self.nombre = nombre
        self._tarifa = 0
        self._capacidad = 1
        self.rutas = []
        self.set_tarifa(tarifa)
        self.set_capacidad(capacidad)

    # Getters
    def get_tarifa(self):
        return self._tarifa

    def get_capacidad(self):
        return self._capacidad

    # Setters con validaciones
    def set_tarifa(self, tarifa):
        if not isinstance(tarifa, (int, float)) or tarifa < 0:
            raise ValueError("La tarifa debe ser un número no negativo")
        self._tarifa = tarifa

    def set_capacidad(self, capacidad):
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero mayor que cero")
        self._capacidad = capacidad

    def agregar_ruta(self, ruta):
        if not isinstance(ruta, Ruta):
            raise TypeError("Se debe agregar un objeto Ruta")
        self.rutas.append(ruta)

    def mostrar_informacion(self):
        print(f"Transporte: {self.nombre}")
        print(f"Tarifa de ejemplo: ${self.get_tarifa():.2f}")  # 2f consulta es para que se muestre el main con 2 decimales
        print(f"Capacidad de ejemplo: {self.get_capacidad()}")

    def mostrar_rutas(self):
        if not self.rutas:
            print("Sin rutas registradas")
        for ruta in self.rutas:
            ruta.mostrar_paradas()
