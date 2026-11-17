# Andina Market 360 · Ventas por sede y dashboard académico

[![Pruebas](https://github.com/JOSEJULIAN99/andina-market-360/actions/workflows/ci.yml/badge.svg)](https://github.com/JOSEJULIAN99/andina-market-360/actions/workflows/ci.yml)
[![Publicar Pages](https://github.com/JOSEJULIAN99/andina-market-360/actions/workflows/pages.yml/badge.svg)](https://josejulian99.github.io/andina-market-360/)

Proyecto integrador del **Cuaderno de prácticas Git y GitHub (36 capítulos)**, desarrollado por nuestro grupo del curso **Herramientas de Desarrollo (UTP)**.

## Objetivo
Convertir un CSV de ventas **simuladas** de una cadena ficticia (Lima, Ica y Arequipa) en un resumen verificable por sede y una página web estática. Nunca incorporamos datos reales de personas.

**Sitio publicado:** https://josejulian99.github.io/andina-market-360/

## Resultados verificados
| Sede | Total (S/) |
|---|---|
| Lima | 814.00 |
| Ica | 555.00 |
| Arequipa | 476.00 |
| **Total (12 operaciones)** | **1845.00** |

## Estructura
| Ruta | Contenido |
|---|---|
| `data/ventas.csv` | 12 transacciones ficticias |
| `src/resumen.py` | procesamiento con Python estándar (sin librerías de terceros) |
| `tests/test_resumen.py` | 5 pruebas unitarias |
| `docs/` | sitio estático para GitHub Pages ([manual](docs/manual.md)) |
| `gestion/` | proyecto, plan final, riesgos, gobernanza, IA responsable y notas de versión |
| `.github/` | workflows (CI, Pages, Release), plantillas, CODEOWNERS y Dependabot |

## Instrucciones
```bash
git clone https://github.com/JOSEJULIAN99/andina-market-360.git
cd andina-market-360
python -m unittest discover -s tests -v
python src/resumen.py --json docs/data/resumen.json
python -m http.server 8000 --directory docs
```
Abrir `http://localhost:8000` mientras se ejecuta el servidor. Detener con Ctrl+C.

## Flujo de trabajo del equipo
Issue → rama `feature/*` o `fix/*` → commit → Pull Request → revisión de Calidad → CI en verde → merge → Pages → tag y Release. Ver [CONTRIBUTING.md](CONTRIBUTING.md).

## Equipo
| Integrante | GitHub | Rol |
|---|---|---|
| Altamirano | [@xxsebas15xx](https://github.com/xxsebas15xx) | Calidad y CI |
| Sofía | [@sofia067](https://github.com/sofia067) | Desarrollo del script |
| Junior | [@JuniorAlonso](https://github.com/JuniorAlonso) | Datos, documentación y web |
| José | [@JOSEJULIAN99](https://github.com/JOSEJULIAN99) | Integración, publicación y seguridad |

## Uso responsable
Proyecto exclusivamente didáctico. No almacenamos contraseñas, tokens, correos personales ni ventas reales. Ver [SECURITY.md](SECURITY.md) y [uso responsable de IA](gestion/ia_responsable.md).

## Fuentes
Documentación de GitHub (docs.github.com), Pro Git en español (git-scm.com/book/es/v2) y el cuaderno de prácticas del curso.
