# Plan de cambios finales (cap. 36)

| # | Actividad | Responsable | Prioridad | Rama | Criterio de aceptación | Depende de |
|---|---|---|---|---|---|---|
| 1 | Datos: validar 12 ventas ficticias | Junior | Alta | `main` (sin cambios) | `python src/resumen.py` → 12 operaciones | — |
| 2 | Script: totales por sede y JSON | Sofía | Alta | `feature/resumen-sedes` | Lima 814 · Ica 555 · Arequipa 476 | 1 |
| 3 | Pruebas: prueba por sede + CI | Altamirano | Alta | `feature/ficha-sedes` | 5/5 pruebas y CI verde en 3 versiones de Python | 2 |
| 4 | Web: Pages con JSON generado | José | Media | `feature/entrega-final` | la página muestra los mismos totales del CSV | 3 |
| 5 | Seguridad: .gitignore, hook, SECURITY, Dependabot | José | Media | `feature/entrega-final` | sin secretos; permisos mínimos en workflows | 3 |

Orden: datos → script → pruebas → publicación. Ningún cambio se hace directamente en `main`: todo entra por Pull Request.
