# Código inicial de la sesión 2

Este directorio contiene el punto de partida común para la segunda sesión. Incluye el resultado completo de la sesión 1: módulo `info`, autenticación, rutas protegidas, catálogo, registro de productos y presentación de existencias agotadas.

La aplicación continúa utilizando datos en memoria. Durante la sesión se conectará con PostgreSQL mediante Docker Compose y SQLAlchemy.

## Antes de iniciar

1. Copiar `.env.example` como `.env`.
2. Activar el entorno virtual.
3. Instalar las dependencias de `requirements.txt`.
4. Ejecutar `python run.py` y confirmar que el resultado de la sesión 1 sigue funcionando.
5. Revisar los bloques marcados como `TODO SESIÓN 2`.

## Archivos de trabajo

| Archivo | Trabajo de la sesión |
|---|---|
| `compose.yaml` | Iniciar y comprobar PostgreSQL |
| `.env` | Cambiar el modo de datos y revisar la conexión |
| `app/models/__init__.py` | Definir los modelos `User` y `Product` |
| `app/models/seed.py` | Crear usuarios y productos iniciales |
| `app/__init__.py` | Inicializar SQLAlchemy, crear tablas y cargar datos |
| `app/auth/store.py` | Sustituir la búsqueda en memoria por consultas SQLAlchemy |
| `app/products/store.py` | Sustituir la lista por consultas y transacciones |
| `app/auth/routes.py` | Adaptar el acceso a los atributos del modelo `User` |
| `app/products/routes.py` | Adaptar el acceso al identificador del modelo `Product` |
| Plantillas | Actualizar los mensajes que todavía indican almacenamiento en memoria |

## Resultado esperado

Al finalizar, los usuarios y productos deberán conservarse después de reiniciar Flask. El formulario y la lógica de venta permanecerán fuera de este código porque corresponden a la práctica posterior.

