# Andina Market 360 · Ventas por sede

Caso ficticio único del **Cuaderno de prácticas Git y GitHub (36 capítulos)**.

## Objetivo
Convertir un CSV de ventas **simuladas** en un resumen verificable por sede y una página web estática. Nunca incorporar datos reales de personas.

## Carpetas
- `data/ventas.csv`: 12 transacciones ficticias.
- `src/resumen.py`: procesamiento con Python sin librerías de terceros.
- `tests/test_resumen.py`: pruebas unitarias locales.
- `docs/`: sitio estático preparado para GitHub Pages.

## Prueba local
```bash
python -m unittest discover -s tests -v
python src/resumen.py --json docs/data/resumen.json
python -m http.server 8000 --directory docs
```
Abrir `http://localhost:8000` mientras se ejecuta el servidor. Detener con Ctrl+C.

## Uso responsable
El proyecto es exclusivamente didáctico. No almacenar contraseñas, tokens, correos personales ni ventas reales.

## Equipo
Grupo de Herramientas de Desarrollo (UTP): Altamirano, Sofía, Junior y José.
