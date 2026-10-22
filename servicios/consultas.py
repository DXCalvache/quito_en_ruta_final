
# QUITO EN RUTA - SERVICIOS DE CONSULTA


def buscar_rutas_directas(transportes, origen, destino):
    """
    Busca rutas donde el origen aparece antes del destino.
    Devuelve una lista de recorridos encontrados.
    """

    origen = origen.strip().casefold()
    destino = destino.strip().casefold()

    resultados = []

    if not origen or not destino or origen == destino:
        return resultados

    for transporte in transportes:
        for ruta in transporte.rutas:

            nombres_paradas = [
                parada.nombre.strip().casefold()
                for parada in ruta.paradas
            ]

            if origen in nombres_paradas and destino in nombres_paradas:

                indice_origen = nombres_paradas.index(origen)
                indice_destino = nombres_paradas.index(destino)

                if indice_origen < indice_destino:
                    recorrido = {
                        "transporte": transporte,
                        "ruta": ruta,
                        "paradas": ruta.paradas[
                            indice_origen:indice_destino + 1
                        ]
                    }

                    resultados.append(recorrido)

    return resultados
