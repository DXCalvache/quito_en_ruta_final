# Proyecto final: Quito en Ruta — Sistema de Transporte Público

Este proyecto integra los contenidos de Programación Orientada a Objetos en una aplicación de consola interactiva desarrollada en Python.

El sistema permite consultar información sobre los transportes públicos de Quito, sus tarifas, capacidades, rutas y paradas. Además, permite registrar rutas, agregar paradas, buscar recorridos directos y generar resúmenes generales.

## Ejecución

Abra la carpeta `quito_en_ruta_final` en Visual Studio Code y ejecute:

```text
python main.py
```

Para ejecutar las pruebas:

```text
python -m pruebas.test_proyecto
```

## Conceptos señalados en el código

- Abstracción y responsabilidades: `modelos/transporte_publico.py`.
- Encapsulación y validaciones: `modelos/transporte_publico.py`.
- Asociación y agregación: `modelos/transporte_publico.py` y `modelos/ruta.py`.
- Herencia: Metro, Trolebus, Ecovia y Bus derivan de `TransportePublico`.
- Sobrescritura: cada transporte redefine `mostrar_informacion()`.
- Polimorfismo: `main.py` utiliza `mostrar_informacion()` con diferentes transportes.
- Getters y setters: métodos para consultar y modificar tarifas y capacidades.
- Excepciones: validaciones mediante `ValueError` y `TypeError`.
- Módulos: las clases están distribuidas en el paquete `modelos/`.
- Servicios: `servicios/consultas.py` realiza la búsqueda de recorridos.
- Pruebas: `pruebas/test_proyecto.py`.

Los comentarios con etiquetas como `[AGREGACIÓN]`, `[POLIMORFISMO]` y `[SERVICIOS]` permiten identificar los conceptos implementados.
