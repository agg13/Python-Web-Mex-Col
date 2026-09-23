# Proyecto inicial — Sesión 1

Este es el punto de partida del proyecto. La aplicación se puede instalar y ejecutar, pero la lógica principal de autenticación y productos está intencionalmente incompleta para desarrollarla durante el taller.

## Manuales incluidos

La carpeta `manuales` contiene materiales dirigidos a cualquier persona que revise o ejecute el repositorio:

- [Preparación del entorno](manuales/preparacion_entorno.md).
- [Guía rápida de Linux](manuales/guia_rapida_linux.md).
- [Guía de apoyo: Flask, Jinja2 y WTForms](manuales/guia_flask_jinja_wtforms.md).
- [Lista de comprobación previa](manuales/lista_comprobacion_previa.md).

Los manuales indican su versión y fecha de publicación, y se actualizarán conforme avance el proyecto.

## Qué está preparado

- Estructura modular de Flask.
- Fábrica `create_app`.
- Configuración y variables de entorno.
- Blueprints de inicio, autenticación y productos.
- Formularios y validadores.
- Plantillas y estilos.
- Dos usuarios didácticos con contraseñas convertidas a hash.
- Catálogo ficticio de 20 productos.
- Funciones auxiliares para consultar y agregar productos en memoria.
- Espacio para modelos SQLAlchemy.
- Variables previstas para PostgreSQL.

## Qué está incompleto intencionalmente

Los archivos contienen comentarios `TODO SESIÓN 1` para completar:

- autenticación de credenciales;
- creación de la sesión;
- cierre de sesión;
- protección de rutas;
- envío del catálogo a la plantilla;
- conexión del formulario con el registro en memoria;
- presentación de productos agotados.
- creación de un módulo `info`, su blueprint, la ruta `/info` y su plantilla.

## Resultado inicial

Al ejecutar el proyecto se muestra una página de preparación. Se puede abrir el formulario de login y las rutas de productos, pero todavía no existe un flujo funcional completo.

Esto permite comprobar instalación y estructura antes de comenzar, sin entregar resuelta la actividad principal.

## Preparación

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
```

## Ejecución

```bash
python run.py
```

Abrir <http://127.0.0.1:5001>.

## Credenciales que se utilizarán durante el taller

| Dato | Valor |
|---|---|
| Usuario | `alumno` |
| Contraseña | `Taller2026!` |

## Archivos principales de trabajo

| Archivo | Trabajo previsto |
|---|---|
| `app/auth/store.py` | Completar la comprobación de credenciales |
| `app/auth/routes.py` | Crear sesión, proteger rutas y cerrar sesión |
| `app/products/routes.py` | Enviar catálogo y registrar productos |
| `app/templates/products/list.html` | Mostrar productos agotados |
| `app/info/` y `app/templates/info/` | Crear un módulo mínimo, su ruta y su plantilla |
| `app/__init__.py` | Registrar el nuevo blueprint `info_bp` |

## Preparación para la sesión 2

- `config.py` reconoce `DATA_MODE` y `DATABASE_URL`.
- `app/extensions.py` declara `db`.
- `app/models` reserva el lugar de `User` y `Product`.
- Los nombres de los diccionarios coinciden con los atributos previstos de `Product`.

No cambiar `DATA_MODE=database` durante la sesión 1.

