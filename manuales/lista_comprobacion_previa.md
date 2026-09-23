# Lista de comprobación previa

**Versión del manual:** 1  
**Fecha de publicación:** 23 de septiembre de 2026  
**Evolución:** esta lista se irá mejorando conforme avance el proyecto y cambien sus requisitos técnicos.

## 1. Objetivo

Confirmar que el entorno puede ejecutar el proyecto antes de comenzar las actividades de desarrollo.

Completa la lista después de seguir el manual de [Preparación del entorno](preparacion_entorno.md). Si necesitas recordar un comando, consulta la [Guía rápida de Linux](guia_rapida_linux.md).

## 2. Sistema Linux

- [ ] Utilizo Ubuntu 24.04 LTS o Debian 12.
- [ ] Puedo abrir una terminal Bash.
- [ ] `cat /etc/os-release` muestra la distribución y versión.
- [ ] `uname -m` muestra la arquitectura.
- [ ] Puedo utilizar `pwd`, `ls` y `cd`.
- [ ] Tengo espacio disponible para el repositorio, dependencias e imágenes de Docker.

## 3. Python

- [ ] `python3 --version` muestra una versión de Python 3.
- [ ] `python3 -m pip --version` funciona.
- [ ] `python3 -m venv .venv` crea el entorno virtual.
- [ ] `source .venv/bin/activate` activa el entorno.
- [ ] La terminal muestra `(.venv)` o `which python` apunta a `.venv`.
- [ ] `python -m pip install -r requirements.txt` termina sin errores.
- [ ] Puedo salir del entorno mediante `deactivate`.

## 4. Git y GitHub

- [ ] `git --version` funciona.
- [ ] Configuré `user.name` y `user.email`.
- [ ] Puedo iniciar sesión en GitHub.
- [ ] Mi correo de GitHub está confirmado.
- [ ] Puedo abrir el repositorio desde el navegador.
- [ ] Cloné el repositorio mediante Git.
- [ ] `git status` reconoce el repositorio.
- [ ] Creé o seleccioné mi rama de trabajo.
- [ ] `git branch --show-current` muestra la rama esperada.

## 5. Configuración local del proyecto

- [ ] Estoy ubicado en la raíz del repositorio.
- [ ] Existen `README.md`, `requirements.txt`, `run.py` y la carpeta `app`.
- [ ] Creé `.env` a partir de `.env.example`.
- [ ] `DATA_MODE` conserva el valor `memory` para la primera sesión.
- [ ] `.env` no aparece como archivo preparado para commit.
- [ ] `.venv` no aparece como archivo preparado para commit.
- [ ] No guardé contraseñas ni tokens dentro del código.

## 6. Aplicación Flask

- [ ] Activé `.venv`.
- [ ] Ejecuté `python run.py`.
- [ ] La terminal mostró que el servidor inició sin errores.
- [ ] Abrí en el navegador la dirección mostrada por Flask.
- [ ] La página inicial del proyecto se muestra correctamente.
- [ ] Detuve el servidor con `Ctrl+C`.

## 7. Editor y navegador

- [ ] Dispongo de un editor para Python, HTML, CSS, Markdown y YAML.
- [ ] El editor abre la carpeta completa del repositorio.
- [ ] Puedo localizar `app/__init__.py`.
- [ ] Puedo localizar `app/auth`, `app/products` y `app/templates`.
- [ ] Dispongo de una versión reciente de Chrome, Firefox o Brave.

## 8. Docker para sesiones posteriores

Docker no es necesario para el catálogo en memoria de la primera sesión, pero debe quedar preparado para PostgreSQL.

- [ ] `docker --version` funciona.
- [ ] `docker compose version` funciona.
- [ ] `sudo systemctl status docker` muestra el servicio activo.
- [ ] `sudo docker run hello-world` termina correctamente.
- [ ] Comprendo que los volúmenes pueden contener datos persistentes.
- [ ] Evitaré `docker compose down -v` salvo que quiera borrar deliberadamente esos datos.

## 9. Comprobación de seguridad básica

- [ ] No publicaré `.env`.
- [ ] No registraré `.venv` ni `__pycache__`.
- [ ] No incluiré contraseñas, tokens o claves en commits.
- [ ] Revisaré `git diff` antes de preparar archivos.
- [ ] Revisaré `git diff --staged` antes de cada commit.
- [ ] No ejecutaré comandos destructivos sin revisar primero la ruta exacta.
- [ ] No usaré `sudo` para editar o ejecutar archivos habituales del repositorio.

## 10. Diagnóstico rápido

Si una comprobación falla, registra esta información antes de modificar más elementos:

| Dato | Respuesta |
|---|---|
| Distribución y versión | |
| Arquitectura | |
| Carpeta actual (`pwd`) | |
| Rama actual | |
| Comando ejecutado | |
| Mensaje completo | |
| Resultado esperado | |
| Acciones ya intentadas | |

No incluyas contraseñas, tokens, claves ni el contenido completo de `.env`.

## 11. Resultado final

Marca una opción:

- [ ] **Listo:** puedo clonar, crear una rama, instalar dependencias y ejecutar la aplicación.
- [ ] **Listo para la primera sesión:** Flask funciona, pero Docker todavía requiere atención antes de la sesión de PostgreSQL.
- [ ] **Requiere atención:** existe un problema que impide ejecutar el proyecto.

Si seleccionaste **Requiere atención**, conserva el diagnóstico de la sección anterior y evita repetir instalaciones o eliminar archivos sin identificar primero la causa.

