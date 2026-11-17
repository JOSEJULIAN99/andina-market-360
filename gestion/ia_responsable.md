# Uso responsable de IA (cap. 32)

**Prompt verificable que usamos:** "Mejora el README sin inventar cifras, sin cambiar el CSV y sin incluir secretos."

**Validación obligatoria:** ejecutar `python -m unittest discover -s tests -v` y revisar `git diff` antes de confirmar.

Reglas del grupo:
1. La IA propone; un integrante revisa y firma el commit.
2. Ninguna cifra sale de la IA: todas salen de `src/resumen.py`.
3. No pegamos tokens, contraseñas ni datos reales en un asistente.
4. Documentamos en el PR qué parte fue asistida.
