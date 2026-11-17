# Guía de contribución

1. Abrimos o elegimos un **Issue** con criterio de aceptación (entrada → cambio → prueba → resultado).
2. Creamos una rama desde `main`: `feature/<tema>` o `fix/<tema>`. Nunca editamos `main` directamente.
3. Antes de confirmar ejecutamos:
   ```bash
   python -m unittest discover -s tests -v
   python src/resumen.py --json docs/data/resumen.json
   git status --short
   ```
4. Mensajes de commit en español con prefijo: `feat:`, `fix:`, `docs:`, `test:`, `ci:`, `chore:`.
5. Abrimos un **Pull Request** con la plantilla, enlazamos el Issue (`Closes #N`) y pedimos revisión a Calidad.
6. Solo fusionamos con la CI en verde y sin conflictos.

**Prohibido** subir contraseñas, tokens, claves privadas o datos de personas reales.
