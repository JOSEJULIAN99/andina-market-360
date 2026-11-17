# Manual de uso · Andina Market 360

## Indicadores calculados
| Indicador | Origen | Comando |
|---|---|---|
| Operaciones | filas de `data/ventas.csv` | `python src/resumen.py` |
| Total por sede | suma de cantidad × precio | `python src/resumen.py` |
| Sede líder / producto más vendido | `src/resumen.py` | `python src/resumen.py` |
| JSON para la web | `docs/data/resumen.json` | `python src/resumen.py --json docs/data/resumen.json` |

## Rutas relativas
- La página [`index.html`](index.html) lee [`data/resumen.json`](data/resumen.json) con una ruta **relativa**, por eso funciona igual en `localhost:8000` y en GitHub Pages.
- Volver al [README](../README.md).
