# Política de seguridad

- El repositorio solo contiene **datos ficticios**. No hay dependencias de terceros en Python.
- Nunca subimos `.env`, claves privadas ni tokens (ver `.gitignore`).
- Las cuentas del equipo usan **2FA**; la autenticación de Git es por HTTPS con credencial gestionada o por SSH con clave protegida por frase.
- Los workflows usan `permissions` mínimos (`contents: read` salvo despliegue/release).

## Reporte responsable
Si encuentras una vulnerabilidad o un secreto expuesto, **no abras un Issue público**: usa *Security → Report a vulnerability* del repositorio. Respondemos en un máximo de 72 horas.

## Respuesta ante una credencial filtrada (simulacro)
1. Revocar el token en *Settings → Developer settings*.
2. Generar uno nuevo con el alcance mínimo y fecha de caducidad.
3. Eliminar el secreto del código y documentar el incidente sin copiar el valor.
