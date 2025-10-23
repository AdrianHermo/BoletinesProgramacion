# Supermercado: control de efectivo por caja

def main():
    # Cada tupla representa una caja con los importes de los billetes en efectivo
    # Ejemplo: (billetes de 10€, 20€, 50€, etc.)
    cajas = [
        ("Caja 1", [10, 20, 10, 5, 50]),
        ("Caja 2", [5, 5, 10, 20, 20, 10]),
        ("Caja 3", [50, 20, 10, 100]),
        ("Caja 4", [10, 10, 5, 5])
    ]

    print("=== SUPERMERCADO: CONTROL DE EFECTIVO ===\n")

    total_general = 0

    # Recorremos las cajas
    for nombre, importes in cajas:
        print(f"Contenido de {nombre}: {importes}")
        total_caja = sum(importes)
        print(f"→ Importe total en {nombre}: {total_caja} €\n")
        total_general += total_caja

    print("===========================================")
    print(f"IMPORTE TOTAL EN TODAS LAS CAJAS: {total_general} €")
    print("===========================================")


# Ejecutar el programa
if __name__ == "__main__":
    main()
