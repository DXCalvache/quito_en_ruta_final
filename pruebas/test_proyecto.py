
# PRUEBAS DEL PROYECTO QUITO EN RUTA

from modelos import TransportePublico, Metro, Trolebus, Ecovia, Bus
from modelos import Ruta, Parada


def ejecutar_pruebas():

    # [HERENCIA] Comprobamos que Metro hereda de TransportePublico
    metro = Metro("Metro de Quito", 0.45, 500, "Línea Sur")
    assert isinstance(metro, TransportePublico)

    # [ENCAPSULAMIENTO] Comprobamos getters y setters
    assert metro.get_tarifa() == 0.45
    assert metro.get_capacidad() == 500

    metro.set_tarifa(0.50)
    assert metro.get_tarifa() == 0.50

    # [VALIDACIÓN] Una tarifa negativa debe generar ValueError
    try:
        metro.set_tarifa(-1)
        assert False, "Se aceptó una tarifa negativa"
    except ValueError:
        pass

    # [AGREGACIÓN] Creamos una ruta y sus paradas
    ruta = Ruta("M-01", "Recorrido Sur a Norte")

    parada_1 = Parada("El Labrador", "Norte")
    parada_2 = Parada("La Carolina", "Centro-norte")

    ruta.agregar_parada(parada_1)
    ruta.agregar_parada(parada_2)

    assert len(ruta.paradas) == 2
    assert ruta.paradas[0].nombre == "El Labrador"

    # Asociamos la ruta al Metro
    metro.agregar_ruta(ruta)
    assert len(metro.rutas) == 1

    # [POLIMORFISMO] Diferentes clases comparten el mismo método
    transportes = [
        metro,
        Trolebus("Trolebús", 0.35, 160, "Corredor Central"),
        Ecovia("Ecovía", 0.35, 160, "Corredor Oriental"),
        Bus("Bus convencional", 0.35, 60, "Vingala")
    ]

    for transporte in transportes:
        assert isinstance(transporte, TransportePublico)
        assert callable(transporte.mostrar_informacion)

    
    # [SERVICIOS] Pruebas de búsqueda de recorridos
    from servicios import buscar_rutas_directas

    # Usamos la lista de transportes creada anteriormente
    # y la ruta M-01 que asignamos al Metro.

    resultados = buscar_rutas_directas(
        transportes, "El Labrador", "La Carolina"
    )

    assert len(resultados) == 1
    assert resultados[0]["transporte"] is metro
    assert resultados[0]["ruta"] is ruta
    assert len(resultados[0]["paradas"]) == 2

    # Buscar en sentido contrario no debe encontrar la ruta
    resultados_inversos = buscar_rutas_directas(
        transportes, "La Carolina", "El Labrador"
    )
    assert resultados_inversos == []

    # Una parada inexistente no debe producir resultados
    resultados_inexistentes = buscar_rutas_directas(
        transportes, "El Labrador", "Parada inexistente"
    )
    assert resultados_inexistentes == []

    # La búsqueda no distingue mayúsculas y minúsculas
    resultados_minusculas = buscar_rutas_directas(
        transportes, "el labrador", "LA CAROLINA"
    )
    assert len(resultados_minusculas) == 1

    print("¡Todas las pruebas finalizaron correctamente!")


if __name__ == "__main__":
    ejecutar_pruebas()
