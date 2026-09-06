#Lista de diccionarios con datos de cultivos
cultivos=[
    {"nombre": "Café", "hectareas":5.0, "produccion_toneladas":3.2},
    {"nombre": "Caña de azúcar", "hectareas":10.0, "produccion_toneladas":8.5},
    {"nombre": "Maíz", "hectareas":7.5, "produccion_toneladas":6.0},
    {"nombre": "Platano", "hectareas":4.0, "produccion_toneladas":2.5},
    {"nombre": "Cacao", "hectareas":3.0, "produccion_toneladas":1.8}
]

def calcular_rendimiento(cultivo):
    """Retorna el rendimiento en toneladas por hectárea de un cultivo dado."""
    return cultivo["produccion_toneladas"] / cultivo["hectareas"]

def mostrar_cultivos(lista_cultivos):
    """Recorre la lista de cultivos e imprime el nombre y rendimiento de cada uno."""
    print("=== Rendimiento de Cultivos ===")
    for cultivo in lista_cultivos:
        rendimiento = calcular_rendimiento(cultivo)
        print(f"-{cultivo['nombre']}: {rendimiento:.2f} toneladas/ha")

def cultivo_mayor_rendimiento(lista_cultivos):
    """Retorna el nombre del cultivo con mayor rendimiento por hectárea."""
    mayor_cultivo=None
    mayor_rendimiento=0.0

    for cultivo in lista_cultivos:
        rend=calcular_rendimiento(cultivo)
        if rend>mayor_rendimiento:
            mayor_rendimiento=rend
            mayor_cultivo=cultivo["nombre"]

    return mayor_cultivo

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # 1. Llamar a la funcion para mostrar todos los cultivos
    mostrar_cultivos(cultivos)

    print() #Imprime una línea en blanco

    # 2. Obtener y mostrar el cultivo con mayor rendimiento
    mejor= cultivo_mayor_rendimiento(cultivos)
    print(f"El cultivo con mayor rendimiento es: {mejor}")

    