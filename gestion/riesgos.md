# Riesgos y mitigación (Reto 36.2)

| # | Riesgo | Mitigación | Evidencia del control |
|---|---|---|---|
| 1 | Subir un token o contraseña | `.gitignore`, hook pre-commit, SECURITY.md | Hook bloqueó un token simulado (CAP33_E05) |
| 2 | Cifras escritas a mano en la web | La web solo lee `docs/data/resumen.json` generado por Python | `git diff` y prueba de humo de Pages |
| 3 | Fusionar código roto | CI con matriz 3.11-3.13 y política "solo verde" | Ejecución roja → corrección → verde en el PR |
| 4 | Perder historial o una versión | `git revert`, `reflog`, `git bundle`, tag v1.0.0 | CAP10_E03, CAP27_E04, Release v1.0.0 |
| 5 | Conflictos entre integrantes | Ramas por tarea, PR con revisión, CODEOWNERS | Conflicto resuelto (CAP10_E02) y PR revisado |
