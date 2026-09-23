# Preparación del entorno de desarrollo

**Versión del manual:** 1  
**Fecha de publicación:** 23 de septiembre de 2026  
**Evolución:** este manual se irá mejorando conforme avance el proyecto y se incorporen nuevas herramientas o necesidades.

## 1. Objetivo

Preparar una computadora con Linux para ejecutar y modificar el proyecto de tienda didáctica durante la primera sesión y las sesiones posteriores.

Al terminar deberás contar con:

- Ubuntu 24.04 LTS o Debian 12;
- una terminal Bash;
- Python 3, `pip` y entornos virtuales;
- Git configurado;
- acceso a GitHub;
- Docker Engine y Docker Compose;
- un editor de código;
- un navegador actualizado;
- una copia local del repositorio.

> Los comandos de este manual deben ejecutarse en una terminal. No copies el símbolo `$` si aparece en otros materiales.

## 2. Identificar el sistema

Ejecuta:

```bash
cat /etc/os-release
uname -m
```

El primer comando muestra la distribución y versión. El segundo muestra la arquitectura, normalmente `x86_64`.

## 3. Actualizar la información de paquetes

```bash
sudo apt update
```

`sudo` solicita la contraseña de tu usuario y permite realizar una operación administrativa. No lo utilices en comandos que no lo necesiten.

## 4. Instalar las herramientas básicas

```bash
sudo apt install -y git python3 python3-venv python3-pip curl ca-certificates
```

Comprueba la instalación:

```bash
git --version
python3 --version
python3 -m pip --version
```

Los tres comandos deben mostrar una versión sin producir errores.

## 5. Configurar Git

Sustituye los valores de ejemplo por tu nombre y el correo asociado con GitHub:

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@example.com"
git config --global init.defaultBranch main
```

Comprueba la configuración:

```bash
git config --global --list
```

No escribas contraseñas ni tokens dentro de la configuración del repositorio.

## 6. Preparar GitHub

Antes de clonar el proyecto:

1. inicia sesión en <https://github.com>;
2. confirma el correo de la cuenta;
3. verifica que puedes abrir la página del repositorio;
4. copia su dirección desde el botón **Code**;
5. selecciona la dirección HTTPS si todavía no utilizas claves SSH.

## 7. Instalar Docker

Docker se utilizará en sesiones posteriores para ejecutar PostgreSQL. Realiza la instalación con la guía oficial correspondiente:

- Ubuntu: <https://docs.docker.com/engine/install/ubuntu/>
- Debian: <https://docs.docker.com/engine/install/debian/>
- Configuración posterior en Linux: <https://docs.docker.com/engine/install/linux-postinstall/>

La instalación debe incluir Docker Engine y el complemento Docker Compose.

Comprueba:

```bash
docker --version
docker compose version
sudo systemctl status docker
sudo docker run hello-world
```

Si el estado se abre en una pantalla de consulta, presiona `q` para regresar a la terminal.

No ejecutes scripts de instalación obtenidos de sitios no oficiales. Tampoco uses `docker compose down -v` sin comprender que puede eliminar los datos almacenados en volúmenes.

## 8. Preparar el editor y el navegador

Puedes utilizar un editor compatible con Python, HTML, CSS, Markdown y YAML. Visual Studio Code o VSCodium ofrecen una configuración sencilla, pero el proyecto no depende de un editor específico.

Utiliza una versión reciente de Chrome, Firefox o Brave.

## 9. Clonar el repositorio

Ubícate en la carpeta donde conservarás el proyecto:

```bash
mkdir -p ~/proyectos
cd ~/proyectos
git clone URL_DEL_REPOSITORIO
cd NOMBRE_DEL_REPOSITORIO
```

Sustituye `URL_DEL_REPOSITORIO` y `NOMBRE_DEL_REPOSITORIO` por los valores reales.

Comprueba que estás dentro del repositorio:

```bash
git status
```

## 10. Crear una rama de trabajo

Utiliza tu nombre de usuario de GitHub en minúsculas:

```bash
git switch -c taller/usuario-github-sesion-1
git branch --show-current
```

Trabaja en esta rama y evita realizar cambios directamente en `main`.

## 11. Crear el entorno virtual del proyecto

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Cuando el entorno está activo, la terminal suele mostrar `(.venv)` al inicio de la línea.

Utiliza `python` y `python -m pip` mientras `.venv` esté activo. Para salir:

```bash
deactivate
```

La carpeta `.venv` es local: no debe copiarse ni registrarse en Git.

## 12. Crear la configuración local

```bash
cp .env.example .env
```

El archivo `.env.example` documenta los valores esperados. El archivo `.env` contiene la configuración local y no debe publicarse.

Durante la primera sesión conserva:

```text
DATA_MODE=memory
```

No cambies todavía el proyecto al modo de base de datos.

## 13. Ejecutar la aplicación

Activa el entorno si fuera necesario y ejecuta:

```bash
source .venv/bin/activate
python run.py
```

La terminal mostrará la dirección local. Con la configuración inicial normalmente será:

<http://127.0.0.1:5001>

Abre esa dirección en el navegador. Para detener Flask, regresa a la terminal y presiona `Ctrl+C`.

## 14. Comprobaciones finales

Antes de trabajar en el código confirma:

```bash
git branch --show-current
python --version
python -m pip --version
git status
```

También comprueba que:

- la aplicación inicia sin errores;
- la página inicial abre en el navegador;
- `.env` y `.venv` no aparecen como archivos preparados para commit;
- puedes localizar `app/`, `requirements.txt` y `run.py`.

Completa después la [lista de comprobación previa](lista_comprobacion_previa.md).

## 15. Información útil cuando ocurre un error

Antes de pedir apoyo conserva:

- el comando exacto que ejecutaste;
- el mensaje completo del error;
- la carpeta actual, obtenida con `pwd`;
- las versiones de Python, Git o Docker relacionadas;
- lo que esperabas que ocurriera;
- los cambios que ya intentaste.

No compartas contraseñas, tokens, claves, contenido de `.env` ni datos personales innecesarios.

## Referencias oficiales

- Python `venv`: <https://docs.python.org/3/library/venv.html>
- Git: <https://git-scm.com/doc>
- GitHub, clonar repositorios: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>
- Docker Engine: <https://docs.docker.com/engine/install/>

