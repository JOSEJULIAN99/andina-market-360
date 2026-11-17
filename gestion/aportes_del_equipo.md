# Procedimiento para que cada integrante figure como aportante en GitHub

Repositorio: https://github.com/JOSEJULIAN99/andina-market-360

GitHub solo cuenta como **contributor** a quien es **autor** de commits que llegan a `main`. Por eso cada integrante debe hacer su propio commit con su cuenta y abrir su propio Pull Request. José ya envió las invitaciones como colaboradores.

| Integrante | Cuenta | Issue | Rama | Archivo |
|---|---|---|---|---|
| Sofía | sofia067 | #15 Ticket promedio por sede | `feature/ticket-promedio` | `src/resumen.py` |
| Altamirano | xxsebas15xx | #16 Prueba de calidad de datos | `test/calidad-datos` | `tests/test_resumen.py` |
| Junior | JuniorAlonso | #17 Sede líder y producto en la web | `feature/web-indicadores` | `docs/index.html`, `docs/app.js` |

**Orden recomendado:** Sofía → Altamirano → Junior (cada uno empieza después de que José fusione el PR anterior y hace `git pull`). Si trabajan a la vez también funciona, porque tocan archivos distintos, salvo Sofía y Junior que no se pisan.

---

## Paso 0 (los tres) · Aceptar la invitación y preparar Git

1. Entrar a https://github.com/JOSEJULIAN99/andina-market-360/invitations (o al correo de GitHub) y pulsar **Accept invitation**.
2. Tener instalados Git y Python 3. En una terminal (Git Bash, PowerShell o Terminal):

```bash
git --version
python --version
git config --global user.name "SU_USUARIO_GITHUB"
git config --global user.email "SU_CORREO_REGISTRADO_EN_GITHUB"
```

> El correo debe ser uno verificado en *GitHub → Settings → Emails*. Si el correo no coincide, el commit no se asocia a su cuenta y **no aparecerá como contributor**. Si prefieren no exponer su correo, usen el correo `...@users.noreply.github.com` que aparece en esa misma página.

3. Clonar y comprobar:

```bash
git clone https://github.com/JOSEJULIAN99/andina-market-360.git
cd andina-market-360
python -m unittest discover -s tests -v
```

Al hacer el primer `git push`, GitHub abrirá una ventana para iniciar sesión (Git Credential Manager). Nunca escriban tokens dentro de archivos.

---

## Sofía (@sofia067) · Issue #15 · Ticket promedio por sede

```bash
git switch main && git pull
git switch -c feature/ticket-promedio
```

En `src/resumen.py`, **justo antes** de `def construir_resumen(ventas):`, pegar:

```python
def ticket_promedio(ventas):
    """Venta promedio por operación en cada sede (Reto 1.1)."""
    operaciones = {}
    for venta in ventas:
        operaciones[venta["sede"]] = operaciones.get(venta["sede"], 0) + 1
    return {s: t / operaciones[s] for s, t in totales_por_sede(ventas).items()}
```

Y dentro de `construir_resumen`, encima de la línea `"fuente": ...`, agregar:

```python
        "ticket_promedio": {s: f"{t:.2f}" for s, t in ticket_promedio(ventas).items()},
```

Comprobar, confirmar y subir:

```bash
python src/resumen.py --json docs/data/resumen.json
python -m unittest discover -s tests -v
git add src/resumen.py docs/data/resumen.json
git commit -m "feat: ticket promedio por sede (closes #15)"
git push -u origin feature/ticket-promedio
```

Resultado esperado en el JSON: Lima 203.50 · Ica 138.75 · Arequipa 119.00.

---

## Altamirano (@xxsebas15xx) · Issue #16 · Prueba de calidad de datos

```bash
git switch main && git pull
git switch -c test/calidad-datos
```

En `tests/test_resumen.py`, **justo antes** de `def test_resumen_serializable(self):`, pegar (con 4 espacios de sangría):

```python
    def test_calidad_de_datos(self):
        ids = [v["id"] for v in self.ventas]
        self.assertEqual(len(ids), len(set(ids)), "hay ids repetidos")
        for venta in self.ventas:
            with self.subTest(id=venta["id"]):
                self.assertIn(venta["sede"], {"Lima", "Ica", "Arequipa"})
                self.assertGreater(venta["cantidad"], 0)
                self.assertGreater(venta["precio_unitario"], 0)
```

```bash
python -m unittest discover -s tests -v      # deben salir 6 pruebas OK
git add tests/test_resumen.py
git commit -m "test: validar calidad de datos del CSV (closes #16)"
git push -u origin test/calidad-datos
```

---

## Junior (@JuniorAlonso) · Issue #17 · Indicadores en la web

```bash
git switch main && git pull
git switch -c feature/web-indicadores
```

En `docs/index.html`, dentro de `<section class="kpis">`, después de la tarjeta "Total vendido", agregar:

```html
      <article><h2>Sede líder</h2><p id="sede-lider">–</p></article>
      <article><h2>Producto más vendido</h2><p id="producto">–</p></article>
```

En `docs/app.js`, debajo de la línea `document.getElementById("total").textContent = ...`, agregar:

```js
    document.getElementById("sede-lider").textContent = datos.sede_lider;
    document.getElementById("producto").textContent = datos.producto_mas_vendido;
```

Probar en el navegador y subir:

```bash
python src/resumen.py --json docs/data/resumen.json
python -m http.server 8000 --directory docs     # abrir http://localhost:8000 y luego Ctrl+C
git add docs/index.html docs/app.js
git commit -m "feat(web): mostrar sede líder y producto más vendido (closes #17)"
git push -u origin feature/web-indicadores
```

---

## Paso final (los tres) · Abrir el Pull Request

1. En GitHub aparecerá el botón **Compare & pull request**; pulsarlo.
2. Base `main` ← su rama. Llenar la plantilla (qué cambia, `Closes #N`, casillas de comprobación).
3. Esperar el check **Pruebas** en verde.
4. Avisar a José: él revisa y fusiona (como dueño del repositorio).
5. Tomar captura de: la terminal con las pruebas, su PR con el check verde y su commit en *Commits*. Esas capturas se añaden al informe en la sección "Aportes individuales".

**Comprobación de que ya figuran:** `https://github.com/JOSEJULIAN99/andina-market-360/graphs/contributors` (GitHub puede tardar unas horas en actualizar esta gráfica; la lista de *Contributors* en la portada se actualiza antes).
