"""Quito en Ruta: 

Los datos de tarifas y capacidades son ejemplos para probar el programa.
"""
from modelos import Parada, Ruta, TransportePublico
from modelos import Metro, Trolebus, Ecovia, Bus
from servicios import buscar_rutas_directas

#Demostración de funcionamiento


def crear_datos_iniciales():
    # Creamos los transportes
    metro = Metro("Metro de Quito", 0.45, 500, "Línea Sur de Quito")
    trolebus = Trolebus("Trolebús", 0.35, 160, "Corredor Trolebús")
    ecovia = Ecovia("Ecovía", 0.35, 160, "Corredor Ecovía")
    bus = Bus("Bus convencional", 0.35, 60, "Bus Vingala")

    # Creamos las paradas
    parada_1 = Parada("El Labrador", "Norte")
    parada_2 = Parada("La Carolina", "Centro-norte")

    # Creamos la ruta del Metro
    ruta_metro = Ruta("M-01", "Recorrido Sur a Norte")

    # [AGREGACIÓN] Asociamos las paradas con la ruta
    ruta_metro.agregar_parada(parada_1)
    ruta_metro.agregar_parada(parada_2)

    # [AGREGACIÓN] Asociamos la ruta con el Metro
    metro.agregar_ruta(ruta_metro)

    # Devolvemos los transportes creados
    transportes = [metro, trolebus, ecovia, bus]
    rutas_registradas = [ruta_metro]

    return transportes, rutas_registradas


def mostrar_menu():
    print("\n========== QUITO EN RUTA ==========")
    print("1. Consultar transportes")
    print("2. Consultar rutas y paradas")
    print("3. Buscar un recorrido")
    print("4. Administrar rutas y paradas")
    print("5. Mostrar resumen general")
    print("0. Salir")
    print("===================================")


def consultar_transportes(transportes):
    while True:
        print("\n====== CONSULTAR TRANSPORTES ======")

        # Mostramos los transportes disponibles
        for i, transporte in enumerate(transportes, start=1):
            print(f"{i}. {transporte.nombre}")

        print("0. Volver al menú principal")

        opcion = input("Seleccione un transporte: ").strip()

        if opcion == "0":
            break

        if not opcion.isdigit():
            print("Ingrese una opción válida.")
            continue

        indice = int(opcion) - 1

        if indice < 0 or indice >= len(transportes):
            print("Transporte no encontrado.")
            continue

        transporte = transportes[indice]

        while True:
            print(f"\n====== {transporte.nombre.upper()} ======")
            print("1. Mostrar información general")
            print("2. Consultar tarifa")
            print("3. Consultar capacidad")
            print("4. Consultar rutas y paradas")
            print("0. Volver a transportes")

            seleccion = input("Seleccione una opción: ").strip()

            if seleccion == "1":
                # [POLIMORFISMO]
                transporte.mostrar_informacion()

            elif seleccion == "2":
                print(f"Tarifa: ${transporte.get_tarifa():.2f}")

            elif seleccion == "3":
                print(f"Capacidad: {transporte.get_capacidad()} pasajeros")

            elif seleccion == "4":
                transporte.mostrar_rutas()

            elif seleccion == "0":
                break

            else:
                print("Opción no válida.")

def consultar_rutas(transportes):
    while True:
        print("\n====== CONSULTAR RUTAS Y PARADAS ======")

        # Obtenemos las rutas de todos los transportes
        rutas_disponibles = []

        for transporte in transportes:
            for ruta in transporte.rutas:
                rutas_disponibles.append((transporte, ruta))

        if not rutas_disponibles:
            print("No existen rutas registradas.")
            return

        # Mostramos las rutas disponibles
        for i, (transporte, ruta) in enumerate(rutas_disponibles, start=1):
            print(f"{i}. {ruta.codigo} - {ruta.nombre} ({transporte.nombre})")

        print("0. Volver al menú principal")

        opcion = input("Seleccione una ruta: ").strip()

        if opcion == "0":
            return

        if not opcion.isdigit():
            print("Debe ingresar un número válido.")
            continue

        indice = int(opcion) - 1

        if indice < 0 or indice >= len(rutas_disponibles):
            print("Ruta no encontrada.")
            continue

        transporte, ruta = rutas_disponibles[indice]

        while True:
            print(f"\n====== RUTA {ruta.codigo} ======")
            print(f"Nombre: {ruta.nombre}")
            print(f"Transporte: {transporte.nombre}")

            print("\n1. Mostrar todas las paradas")
            print("2. Consultar cantidad de paradas")
            print("0. Volver a rutas")

            seleccion = input("Seleccione una opción: ").strip()

            if seleccion == "1":
                # [AGREGACIÓN] Utilizamos las paradas de la ruta
                ruta.mostrar_paradas()

            elif seleccion == "2":
                print(f"Cantidad de paradas: {len(ruta.paradas)}")

            elif seleccion == "0":
                break

            else:
                print("Opción no válida.")


def buscar_recorrido(transportes):
    while True:
        print("\n====== BUSCAR UN RECORRIDO ======")
        print("1. Buscar por origen y destino")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            return

        elif opcion == "1":
            origen = input("Ingrese la parada de origen: ").strip()
            destino = input("Ingrese la parada de destino: ").strip()

            if not origen or not destino:
                print("Debe ingresar ambas paradas.")
                continue

            if origen.casefold() == destino.casefold():
                print("El origen y el destino deben ser diferentes.")
                continue

            # [SERVICIOS] Buscamos los recorridos disponibles
            resultados = buscar_rutas_directas(
                transportes, origen, destino
            )

            if resultados:
                for recorrido in resultados:
                    transporte = recorrido["transporte"]
                    ruta = recorrido["ruta"]
                    paradas = recorrido["paradas"]

                    print("\n¡RECORRIDO ENCONTRADO!")
                    print(f"Transporte: {transporte.nombre}")
                    print(f"Ruta: {ruta.codigo} - {ruta.nombre}")
                    print(f"Origen: {paradas[0].nombre}")
                    print(f"Destino: {paradas[-1].nombre}")
                    print(f"Tarifa: ${transporte.get_tarifa():.2f}")

                    print("\nParadas del recorrido:")
                    for parada in paradas:
                        parada.mostrar_parada()

                    print("-" * 35)

            else:
                print("\nNo se encontró una ruta directa registrada.")
                print("Compruebe las paradas o consulte otras rutas.")

        else:
            print("Opción no válida.")



def administrar_rutas(transportes, rutas_registradas):


    while True:
        print("\n====== ADMINISTRAR RUTAS Y PARADAS ======")
        print("1. Registrar nueva ruta")
        print("2. Agregar parada a una ruta")
        print("3. Asignar ruta a un transporte")
        print("4. Ver rutas registradas")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código de la ruta: ").strip()
            nombre = input("Nombre de la ruta: ").strip()

            if not codigo or not nombre:
                print("El código y el nombre son obligatorios.")
                continue

            if any(ruta.codigo.casefold() == codigo.casefold()
                   for ruta in rutas_registradas):
                print("Ya existe una ruta con ese código.")
                continue

            nueva_ruta = Ruta(codigo, nombre)
            rutas_registradas.append(nueva_ruta)

            print("¡Ruta registrada correctamente!")

        elif opcion == "2":
            if not rutas_registradas:
                print("No hay rutas registradas.")
                continue

            for i, ruta in enumerate(rutas_registradas, 1):
                print(f"{i}. {ruta.codigo} - {ruta.nombre}")

            seleccion = input("Seleccione una ruta: ").strip()

            if not seleccion.isdigit():
                print("Ingrese un número válido.")
                continue

            indice = int(seleccion) - 1

            if indice < 0 or indice >= len(rutas_registradas):
                print("Ruta no encontrada.")
                continue

            ruta = rutas_registradas[indice]

            nombre = input("Nombre de la nueva parada: ").strip()
            sector = input("Sector de la parada: ").strip()

            if not nombre or not sector:
                print("Todos los campos son obligatorios.")
                continue

            # [AGREGACIÓN]
            nueva_parada = Parada(nombre, sector)
            ruta.agregar_parada(nueva_parada)

            print("¡Parada agregada correctamente!")

        elif opcion == "3":
            if not rutas_registradas:
                print("No hay rutas registradas.")
                continue

            print("\nRutas disponibles:")
            for i, ruta in enumerate(rutas_registradas, 1):
                print(f"{i}. {ruta.codigo} - {ruta.nombre}")

            seleccion = input("Seleccione una ruta: ").strip()

            if not seleccion.isdigit():
                print("Ingrese un número válido.")
                continue

            indice = int(seleccion) - 1

            if indice < 0 or indice >= len(rutas_registradas):
                print("Ruta no encontrada.")
                continue

            ruta = rutas_registradas[indice]

            print("\nTransportes disponibles:")
            for i, transporte in enumerate(transportes, 1):
                print(f"{i}. {transporte.nombre}")

            seleccion = input("Seleccione un transporte: ").strip()

            if not seleccion.isdigit():
                print("Ingrese un número válido.")
                continue

            indice = int(seleccion) - 1

            if indice < 0 or indice >= len(transportes):
                print("Transporte no encontrado.")
                continue

            transporte = transportes[indice]

            if ruta in transporte.rutas:
                print("Esta ruta ya está asignada al transporte.")
                continue

            # [AGREGACIÓN]
            transporte.agregar_ruta(ruta)

            print("¡Ruta asignada correctamente!")

        elif opcion == "4":
            if not rutas_registradas:
                print("No hay rutas registradas.")
            else:
                for ruta in rutas_registradas:
                    print("-" * 35)
                    ruta.mostrar_paradas()

        elif opcion == "0":
            return

        else:
            print("Opción no válida.")

def mostrar_resumen_general(transportes):
    print("\n========== RESUMEN GENERAL ==========")

    total_rutas = 0
    total_paradas = 0

    for transporte in transportes:
        print("\n" + "-" * 40)

        # [POLIMORFISMO] Cada transporte muestra su información
        transporte.mostrar_informacion()

        # Contamos las rutas de cada transporte
        cantidad_rutas = len(transporte.rutas)
        total_rutas += cantidad_rutas

        print(f"Rutas registradas: {cantidad_rutas}")

        # [AGREGACIÓN] Recorremos las rutas asociadas
        for ruta in transporte.rutas:
            print(f"\nRuta: {ruta.codigo} - {ruta.nombre}")

            cantidad_paradas = len(ruta.paradas)
            total_paradas += cantidad_paradas

            print(f"Cantidad de paradas: {cantidad_paradas}")

            for parada in ruta.paradas:
                parada.mostrar_parada()

    print("\n========== ESTADÍSTICAS ==========")
    print(f"Transportes registrados: {len(transportes)}")
    print(f"Rutas asignadas: {total_rutas}")
    print(f"Paradas contabilizadas: {total_paradas}")
    print("===================================")


def main():
    transportes, rutas_registradas = crear_datos_iniciales()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            consultar_transportes(transportes)

        elif opcion == "2":
            consultar_rutas(transportes)

        elif opcion == "3":
            buscar_recorrido(transportes)

        elif opcion == "4":
            administrar_rutas(transportes, rutas_registradas)

        elif opcion == "5":
            mostrar_resumen_general(transportes)

        elif opcion == "0":
            print("\n¡Gracias por utilizar Quito en Ruta!")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")



if __name__ == "__main__":
    main()
