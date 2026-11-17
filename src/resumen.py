"""Resumen de ventas ficticias de Andina Market 360.

Lee data/ventas.csv y calcula totales por sede usando solo la biblioteca
estándar de Python. Opcionalmente escribe un JSON para la página estática.
"""
import argparse
import csv
import json
from decimal import Decimal
from pathlib import Path

RUTA_CSV = Path(__file__).resolve().parent.parent / "data" / "ventas.csv"


def leer_ventas(ruta=RUTA_CSV):
    """Devuelve la lista de ventas con el importe de cada operación."""
    with open(ruta, encoding="utf-8", newline="") as archivo:
        ventas = []
        for fila in csv.DictReader(archivo):
            fila["cantidad"] = int(fila["cantidad"])
            fila["precio_unitario"] = Decimal(fila["precio_unitario"])
            fila["importe"] = fila["cantidad"] * fila["precio_unitario"]
            ventas.append(fila)
        return ventas


def totales_por_sede(ventas):
    totales = {}
    for venta in ventas:
        totales[venta["sede"]] = totales.get(venta["sede"], Decimal("0")) + venta["importe"]
    return totales

def total_general(ventas):
    return sum((v["importe"] for v in ventas), Decimal("0"))


def producto_mas_vendido(ventas):
    """Producto con más unidades vendidas."""
    unidades = {}
    for venta in ventas:
        unidades[venta["producto"]] = unidades.get(venta["producto"], 0) + venta["cantidad"]
    return max(unidades, key=unidades.get)


def totales_mensuales(ventas):
    meses = {}
    for venta in ventas:
        mes = venta["fecha"][:7]
        meses[mes] = meses.get(mes, Decimal("0")) + venta["importe"]
    return dict(sorted(meses.items()))

def ticket_promedio(ventas):
    """Venta promedio por operación en cada sede (Reto 1.1)."""
    operaciones = {}
    for venta in ventas:
        operaciones[venta["sede"]] = operaciones.get(venta["sede"], 0) + 1
    return {s: t / operaciones[s] for s, t in totales_por_sede(ventas).items()}


def construir_resumen(ventas):
    return {
        "operaciones": len(ventas),
        "total": f"{total_general(ventas):.2f}",
        "sedes": {s: f"{t:.2f}" for s, t in totales_por_sede(ventas).items()},
        "sede_lider": max(totales_por_sede(ventas), key=totales_por_sede(ventas).get),
        "producto_mas_vendido": producto_mas_vendido(ventas),
        "meses": {m: f"{t:.2f}" for m, t in totales_mensuales(ventas).items()},
        "ticket_promedio": {s: f"{t:.2f}" for s, t in ticket_promedio(ventas).items()},
        "fuente": "data/ventas.csv (datos ficticios)",
    }


def main():
    parser = argparse.ArgumentParser(description="Resumen de ventas ficticias")
    parser.add_argument("--json", help="ruta del JSON a generar")
    args = parser.parse_args()
    resumen = construir_resumen(leer_ventas())
    print(f"Operaciones: {resumen['operaciones']}")
    for sede, total in resumen["sedes"].items():
        print(f"{sede}: S/ {total}")
    print(f"TOTAL: S/ {resumen['total']}")
    print(f"Sede líder: {resumen['sede_lider']} · Producto más vendido: {resumen['producto_mas_vendido']}")
    if args.json:
        destino = Path(args.json)
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"JSON generado en {destino}")


if __name__ == "__main__":
    main()
