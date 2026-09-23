# Guía rápida de Linux

**Versión del manual:** 1  
**Fecha de publicación:** 23 de septiembre de 2026  
**Evolución:** este manual se irá mejorando conforme avance el proyecto y aparezcan nuevas necesidades de trabajo en Linux.

## 1. Objetivo

Servir como referencia rápida para trabajar con el proyecto desde una terminal Bash en Ubuntu o Debian.

Linux distingue mayúsculas y minúsculas. `Proyecto`, `proyecto` y `PROYECTO` representan nombres diferentes.

## 2. Reconocer la carpeta actual

| Comando | Finalidad |
|---|---|
| `pwd` | Mostrar la ruta de la carpeta actual |
| `ls` | Listar los archivos visibles |
| `ls -la` | Mostrar también archivos ocultos y detalles |
| `cd carpeta` | Entrar en una carpeta |
| `cd ..` | Subir un nivel |
| `cd ~` | Ir a la carpeta personal |
| `clear` | Limpiar la pantalla |
| `history` | Consultar comandos recientes |

Ejemplo:

```bash
cd ~/proyectos
ls -la
pwd
```

Las rutas con espacios deben escribirse entre comillas:

```bash
cd "Mi proyecto"
```

## 3. Crear carpetas y archivos

| Comando | Finalidad |
|---|---|
| `mkdir nombre` | Crear una carpeta |
| `mkdir -p ruta/subcarpeta` | Crear una ruta completa |
| `touch archivo.py` | Crear un archivo vacío |
| `cp origen destino` | Copiar un archivo |
| `cp -r origen destino` | Copiar una carpeta |
| `mv origen destino` | Mover o renombrar |
| `rm archivo` | Eliminar un archivo |

Ejemplo de la mini actividad de la primera sesión:

```bash
mkdir -p app/info app/templates/info
touch app/info/__init__.py
touch app/info/routes.py
touch app/templates/info/index.html
```

Evita `rm -r` y `rm -rf` mientras no tengas experiencia suficiente. La terminal normalmente elimina los archivos sin enviarlos a la papelera.

Antes de mover, renombrar o eliminar, verifica la ruta con:

```bash
pwd
ls -la
```

## 4. Leer archivos

```bash
cat archivo.txt
less archivo_largo.txt
head archivo.txt
tail archivo.txt
tail -f archivo.log
```

- Sal de `less` con `q`.
- Detén `tail -f` con `Ctrl+C`.
- Utiliza `cat` sólo para archivos razonablemente pequeños.

## 5. Buscar archivos y texto

Buscar archivos Python desde la carpeta actual:

```bash
find . -name "*.py"
```

Buscar una palabra en todos los archivos:

```bash
grep -R "info_bp" .
```

El punto `.` representa la carpeta actual.

## 6. Trabajar con Python

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
deactivate
```

Después de activar `.venv`, usa `python` y `python -m pip`. Así las dependencias se instalan dentro del entorno del proyecto y no globalmente.

Detén una aplicación Flask activa con `Ctrl+C` antes de iniciarla otra vez.

## 7. Consultar procesos y puertos

```bash
ps aux
ss -ltnp
```

Buscar un puerto concreto:

```bash
ss -ltnp | grep 5001
```

Si el puerto configurado está ocupado, detén primero la ejecución anterior. Si no reconoces el proceso, no lo cierres de forma forzada sin revisarlo.

## 8. Servicios del sistema

Docker funciona como un servicio:

```bash
sudo systemctl status docker
sudo systemctl start docker
sudo systemctl restart docker
```

Usa `restart` solamente cuando sea necesario. Sal de la vista de estado con `q`.

## 9. Docker Compose

En las sesiones de base de datos se utilizarán estos comandos:

```bash
docker compose up -d
docker compose ps
docker compose logs
docker compose logs -f
docker compose down
```

| Comando | Resultado |
|---|---|
| `up -d` | Inicia los servicios en segundo plano |
| `ps` | Muestra el estado de los contenedores |
| `logs` | Muestra los mensajes de los servicios |
| `logs -f` | Sigue los mensajes hasta presionar `Ctrl+C` |
| `down` | Detiene y elimina contenedores y red del proyecto |

No utilices `docker compose down -v` a menos que quieras eliminar deliberadamente los volúmenes y sus datos.

## 10. Permisos

```bash
ls -l
chmod +x script.sh
```

No uses `sudo` por costumbre. Las operaciones habituales dentro de tu repositorio, como editar archivos o ejecutar Python, no deberían necesitarlo.

Si los archivos del proyecto pertenecen a `root`, evita continuar creando más archivos con `sudo`. Primero revisa cómo fueron creados.

## 11. Variables de entorno

Definir y consultar una variable temporal:

```bash
export NOMBRE_VARIABLE="valor"
echo "$NOMBRE_VARIABLE"
```

Las variables creadas con `export` desaparecen al cerrar esa terminal. El proyecto utiliza `.env` para conservar su configuración local.

No muestres contraseñas, claves o tokens mediante capturas, commits o mensajes de soporte.

## 12. Comandos básicos de Git

```bash
git status
git branch --show-current
git diff
git diff --staged
git log --oneline -5
```

Antes de un commit:

1. ejecuta `git status`;
2. revisa `git diff`;
3. agrega únicamente los archivos relacionados;
4. revisa `git diff --staged`;
5. crea el commit.

No agregues `.env`, `.venv`, `__pycache__`, contraseñas ni tokens.

## 13. Atajos de teclado útiles

| Atajo | Acción |
|---|---|
| `Ctrl+C` | Detener el proceso actual |
| `Ctrl+L` | Limpiar visualmente la terminal |
| `Ctrl+R` | Buscar un comando anterior |
| `Tab` | Completar nombres de archivos o carpetas |
| Flecha arriba | Recuperar comandos anteriores |

## 14. Obtener ayuda

```bash
comando --help
man comando
```

Ejemplos:

```bash
git --help
man ls
python -m pip --help
```

## 15. Reportar un problema con claridad

Incluye:

- comando ejecutado;
- carpeta actual obtenida con `pwd`;
- mensaje completo;
- versión de la herramienta;
- resultado esperado;
- acciones ya intentadas.

Consulta también [Preparación del entorno](preparacion_entorno.md) y la [Lista de comprobación previa](lista_comprobacion_previa.md).

