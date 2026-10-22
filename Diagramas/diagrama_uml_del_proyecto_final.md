classDiagram
    direction LR

    class TransportePublico {
        <<abstract>>
        #str id_transporte
        #str nombre
        #float costo
        #str tipo
        +obtener_detalles()* str
        +calcular_tiempo_viaje(distancia: float)* float
    }

    class Bus {
        -int capacidad_pasajeros
        +obtener_detalles() str
        +calcular_tiempo_viaje(distancia: float) float
    }

    class Trolebus {
        -str corredor
        +obtener_detalles() str
        +calcular_tiempo_viaje(distancia: float) float
    }

    class Ecovia {
        -str estacion_principal
        +obtener_detalles() str
        +calcular_tiempo_viaje(distancia: float) float
    }

    class Metro {
        -int numero_vagones
        +obtener_detalles() str
        +calcular_tiempo_viaje(distancia: float) float
    }

    class Parada {
        -str nombre
        -str ubicacion
        -list transportes_disponibles
        +agregar_transporte(transporte: TransportePublico) void
        +mostrar_info() str
    }

    class Ruta {
        -str nombre_ruta
        -list paradas
        -TransportePublico transporte
        +agregar_parada(parada: Parada) void
        +calcular_longitud_total() float
    }

    class ConsultasServicio {
        +buscar_transporte_por_tipo(tipo: str) list
        +filtrar_por_parada(parada_nombre: str) list
    }

    TransportePublico <|-- Bus
    TransportePublico <|-- Trolebus
    TransportePublico <|-- Ecovia
    TransportePublico <|-- Metro

    Ruta "1" --> "1" TransportePublico : opera con
    Ruta "1" o-- "*" Parada : contiene
    Parada "*" --> "*" TransportePublico : conecta
    ConsultasServicio ..> TransportePublico : procesa