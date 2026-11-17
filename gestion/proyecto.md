# Proyecto Andina Market 360

**Problema:** las ventas de Lima, Ica y Arequipa se consolidan a mano en hojas sueltas y los informes se corrigen manualmente.
**Usuarios:** gerencia comercial y jefes de sede de Andina Market 360 (empresa ficticia).
**Necesidad:** consolidar ventas y mostrar resultados por sede sin editar informes manualmente.
**Resultado esperado:** un resumen por sede generado por Python desde `data/ventas.csv` y publicado en una página estática.

## Preguntas comerciales
1. ¿Qué sede lidera las ventas?
2. ¿Qué producto vende más?
3. ¿Cómo cambia el total mensual?
4. (Reto 1.1) ¿Qué ticket promedio tiene cada sede? → lo respondería `docs/data/resumen.json`.

## Herramientas
| Herramienta | Tarea en el proyecto |
|---|---|
| Git | Conserva versiones y cambios de archivos en nuestra computadora. |
| GitHub | Aloja el repositorio y permite revisar cambios en equipo (Issues, PR, Actions, Pages). |
| Python | Ejecuta localmente el programa que calcula las ventas. |

Flujo: `archivo → Git local (add/commit) → repositorio remoto (push) → revisión del equipo (PR)`.
Ningún paso depende de que GitHub ejecute el código de ventas: Python corre en local; Actions solo repite las pruebas si lo configuramos.

## Estructura de trabajo
```
andina-market-360/
├── data/      ventas ficticias (CSV)
├── src/       código Python
├── tests/     pruebas unitarias
├── docs/      página web (GitHub Pages)
├── gestion/   planificación y fichas del equipo
└── .github/   colaboración y automatización
```
El dashboard lee `docs/data/resumen.json` generado por Python: así ninguna cifra se escribe a mano.

## Criterios de éxito
| Indicador | Meta | Responsable | Evidencia |
|---|---|---|---|
| Ventas importadas | 12 operaciones | Junior (Datos) | `python src/resumen.py` |
| Totales por sede | Lima 814 · Ica 555 · Arequipa 476 | Sofía (Desarrollo) | salida del script |
| Pruebas | 4/4 en verde (luego 5/5) | Altamirano (Calidad) | `python -m unittest discover -s tests -v` |
| Resumen web | página publicada | José (Integración) | captura de GitHub Pages |

## Roles del equipo (Reto 1.2)
| Integrante | Rol | Responsabilidad | Evidencia de revisión |
|---|---|---|---|
| Altamirano | Calidad y CI | pruebas, workflows, revisión de PR | comentario de revisión en el PR |
| Sofía | Desarrollo | `src/resumen.py`, nuevas funciones | commits en ramas `feature/*` |
| Junior | Datos y documentación | CSV ficticio, README, Markdown | Issues cerrados con evidencia |
| José | Integración y publicación | repositorio, ramas, tags, Pages, seguridad | Release v1.0.0 y Pages |

## Clasificación de acciones (Reto 1.3)
| Acción | Dónde ocurre |
|---|---|
| Guardar una versión con mensaje | Git local (`git commit`) |
| Ver diferencias entre dos versiones | Git local (`git diff`) |
| Abrir un Issue | Plataforma GitHub |
| Revisar y fusionar un Pull Request | Plataforma GitHub |
| Calcular los totales por sede | Herramienta externa (Python) |
