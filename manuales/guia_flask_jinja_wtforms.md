# Guía de apoyo: Flask, Jinja2 y WTForms

**Versión del manual:** 1  
**Fecha de publicación:** 23 de septiembre de 2026  
**Evolución:** este manual se irá mejorando conforme avance el proyecto y se incorporen persistencia, contenedores y nuevas funcionalidades.

## 1. Objetivo

Explicar los elementos principales de la tienda didáctica y servir como referencia para completar las actividades de la primera sesión.

Después de revisar esta guía deberás poder:

- localizar las responsabilidades principales del proyecto;
- explicar cómo Flask crea la aplicación;
- crear y registrar un blueprint;
- relacionar una URL con una función y una plantilla Jinja2;
- comprender el flujo básico de autenticación y sesión;
- reconocer la función de Flask-WTF y WTForms;
- validar y registrar un producto;
- explicar por qué los datos en memoria desaparecen al reiniciar;
- identificar qué cambiará al utilizar SQLAlchemy y PostgreSQL.

Esta aplicación es un ejercicio formativo. El login y el almacenamiento temporal permiten estudiar el flujo general, pero no constituyen una solución lista para producción.

## 2. Preparar y ejecutar el proyecto

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python run.py
```

Si ya existe `.env` o `.venv`, no es necesario volver a crearlos. Durante esta sesión conserva:

```text
DATA_MODE=memory
```

Abre en el navegador la dirección mostrada por Flask. Con la configuración inicial normalmente será <http://127.0.0.1:5001>.

Consulta [Preparación del entorno](preparacion_entorno.md) si alguno de estos pasos falla.

## 3. Organización del proyecto

```text
app/
├── auth/
│   ├── forms.py       formulario de login
│   ├── routes.py      login, logout y protección
│   └── store.py       usuarios temporales y autenticación
├── main/
│   └── routes.py      página inicial
├── products/
│   ├── forms.py       formulario y reglas de productos
│   ├── routes.py      catálogo y registro
│   └── store.py       productos almacenados en memoria
├── models/
│   └── __init__.py    espacio para SQLAlchemy
├── templates/
│   ├── auth/
│   ├── errors/
│   ├── main/
│   ├── products/
│   └── base.html
├── static/css/        estilos
├── __init__.py        fábrica de aplicación
└── extensions.py      CSRF y futura base de datos
config.py              configuración
run.py                 ejecución local
```

Durante la mini actividad se agregan:

```text
app/info/
├── __init__.py
└── routes.py

app/templates/info/
└── index.html
```

No necesitas memorizar la estructura. Debes poder localizar dónde se encuentra cada responsabilidad.

## 4. Fábrica de aplicación

`run.py` llama a `create_app`. Esta función crea una instancia de Flask, carga la configuración, prepara las extensiones y registra los módulos:

```python
def create_app(config_object=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    csrf.init_app(app)

    if app.config["DATA_MODE"] == "database":
        db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)

    return app
```

El proyecto utiliza una fábrica porque permite crear una aplicación configurada sin depender de una única instancia global.

Durante la primera sesión `DATA_MODE` permanece en `memory`, por lo que `db` está declarada pero todavía no se conecta.

## 5. Blueprints

Un blueprint agrupa rutas relacionadas:

- `main_bp`: página inicial;
- `auth_bp`: login y logout;
- `products_bp`: consulta y registro de productos;
- `info_bp`: página informativa creada durante la mini actividad.

Un blueprint puede utilizar un prefijo:

```python
products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products",
)
```

Por ello, una ruta `"/new"` dentro de `products_bp` se publica como `/products/new`.

Crear un blueprint no basta. También debe importarse y registrarse en `create_app`.

## 6. Mini actividad: crear el módulo `/info`

Esta actividad muestra el recorrido completo desde la estructura de carpetas hasta el navegador.

### 6.1 Crear las carpetas y los archivos

Desde la raíz del repositorio:

```bash
mkdir -p app/info app/templates/info
touch app/info/__init__.py
touch app/info/routes.py
touch app/templates/info/index.html
```

`__init__.py` permite reconocer `info` como un paquete de Python.

### 6.2 Declarar el blueprint y la ruta

Escribe en `app/info/routes.py`:

```python
from flask import Blueprint, render_template


info_bp = Blueprint("info", __name__, url_prefix="/info")


@info_bp.get("")
def index():
    """Muestra una página informativa creada durante el taller."""

    return render_template("info/index.html")
```

El prefijo `/info` y la ruta vacía se combinan para publicar `GET /info`.

### 6.3 Crear la plantilla

Escribe en `app/templates/info/index.html`:

```jinja2
{% extends "base.html" %}

{% block title %}Información | Tienda didáctica{% endblock %}

{% block content %}
<section class="page-heading">
    <div>
        <p class="eyebrow">Mini actividad guiada</p>
        <h1>Información del ejercicio</h1>
        <p>Aplicación didáctica para consultar y registrar productos de cómputo.</p>
    </div>
</section>
{% endblock %}
```

La plantilla extiende `base.html`, por lo que reutiliza la estructura general, navegación y estilos.

### 6.4 Registrar el blueprint

Dentro de `create_app`, agrega la importación junto a los demás módulos:

```python
from .info.routes import info_bp
```

Después registra el blueprint:

```python
app.register_blueprint(info_bp)
```

### 6.5 Comprobar

Reinicia la aplicación si fuera necesario y abre `/info`.

El recorrido es:

```text
GET /info
    ↓
info_bp
    ↓
index()
    ↓
templates/info/index.html
    ↓
HTML en el navegador
```

Si aparece un error 404, comprueba que `info_bp` esté registrado. Si aparece `TemplateNotFound`, revisa que la plantilla se encuentre exactamente en `app/templates/info/index.html`.

## 7. Rutas y métodos HTTP

Una ruta relaciona un método y una URL con una función:

```python
@info_bp.get("")
def index():
    return render_template("info/index.html")
```

Las rutas principales del ejercicio son:

| Método | Ruta | Finalidad |
|---|---|---|
| `GET`, `POST` | `/login` | Mostrar y procesar el login |
| `POST` | `/logout` | Cerrar la sesión |
| `GET` | `/info` | Mostrar la página informativa |
| `GET` | `/products` | Consultar el catálogo |
| `GET`, `POST` | `/products/new` | Mostrar y procesar el formulario |

`GET` se utiliza principalmente para consultar. `POST` envía datos que pueden cambiar el estado de la aplicación.

## 8. De una solicitud a una plantilla

Cuando el navegador solicita `/products`, el flujo esperado es:

```text
Navegador solicita GET /products
        ↓
Flask localiza list_products_view
        ↓
La función obtiene list_products()
        ↓
render_template entrega products a Jinja2
        ↓
Jinja2 genera HTML
        ↓
El navegador muestra el catálogo
```

La ruta terminada conecta el almacén con la plantilla:

```python
@products_bp.get("")
@login_required
def list_products_view():
    return render_template(
        "products/list.html",
        products=list_products(),
    )
```

`products=` define el nombre con el que la plantilla recibe la lista.

En el proyecto inicial esta ruta entrega una lista vacía. El bloque `TODO SESIÓN 1` indica el punto que debe completarse.

## 9. Jinja2

Jinja2 genera HTML combinando plantillas y datos.

### 9.1 Mostrar un valor

```jinja2
{{ product.name }}
```

### 9.2 Recorrer elementos

```jinja2
{% for product in products %}
    <p>{{ product.name }}</p>
{% endfor %}
```

### 9.3 Aplicar una condición

```jinja2
{% if product.stock_quantity == 0 %}
    Agotado
{% else %}
    {{ product.stock_quantity }}
{% endif %}
```

Esta condición sólo cambia la presentación. No modifica el producto ni su existencia.

### 9.4 Heredar una plantilla

```jinja2
{% extends "base.html" %}

{% block content %}
    <h1>Contenido de la página</h1>
{% endblock %}
```

`base.html` define la estructura común. Cada página reemplaza bloques específicos.

## 10. Formularios con Flask-WTF y WTForms

WTForms permite declarar campos y validadores mediante clases de Python. Flask-WTF integra esos formularios con Flask y agrega protección CSRF.

Ejemplo simplificado:

```python
class ProductForm(FlaskForm):
    name = StringField(
        "Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, max=120),
        ],
    )

    stock_quantity = IntegerField(
        "Cantidad en almacén",
        validators=[
            InputRequired(message="La cantidad es obligatoria."),
            NumberRange(min=0),
        ],
    )
```

Un formulario se procesa normalmente con:

```python
form = ProductForm()

if form.validate_on_submit():
    # Utilizar los datos ya validados.
    pass
```

`validate_on_submit()` comprueba que:

- la solicitud sea `POST`;
- el token CSRF sea válido;
- los campos puedan convertirse al tipo esperado;
- se cumplan los validadores declarados.

Validar no guarda automáticamente la información. La ruta debe ejecutar la operación correspondiente.

## 11. `DataRequired` e `InputRequired`

`DataRequired` comprueba el valor después de su conversión. En Python, `0` se evalúa como falso, aunque sea una existencia válida.

`InputRequired` comprueba que se haya proporcionado una entrada. Por eso la existencia utiliza:

```python
stock_quantity = IntegerField(
    "Cantidad en almacén",
    validators=[
        InputRequired(
            message="La cantidad en almacén es obligatoria."
        ),
        NumberRange(
            min=0,
            message="La cantidad no puede ser negativa."
        ),
    ],
)
```

Resultado:

| Entrada | Resultado |
|---|---|
| Vacía | Inválida |
| `-1` | Inválida |
| `0` | Válida; representa un producto agotado |
| Entero positivo | Válida |

## 12. Protección CSRF

CSRF significa *Cross-Site Request Forgery*. La protección reduce el riesgo de que otro sitio envíe un formulario en nombre de una persona sin su intención.

Los formularios creados con `FlaskForm` incorporan el token mediante:

```jinja2
{{ form.hidden_tag() }}
```

El formulario de logout también incluye un campo oculto:

```jinja2
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

Si el token falta o no coincide, Flask-WTF rechaza la solicitud.

CSRF no sustituye autenticación, autorización ni validación. Resuelve un riesgo diferente.

## 13. Autenticación básica

Autenticar significa comprobar la identidad presentada. El proyecto utiliza usuarios temporales con contraseñas convertidas a hash.

La función terminada normaliza el usuario, localiza una cuenta activa y comprueba la contraseña:

```python
def authenticate(username, password):
    normalized_username = username.strip().lower()
    user = next(
        (
            item
            for item in _USERS
            if item["username"] == normalized_username
            and item["is_active"]
        ),
        None,
    )

    if user and check_password_hash(
        user["password_hash"], password
    ):
        return user

    return None
```

La contraseña original no se almacena. `check_password_hash` comprueba si el texto capturado corresponde al hash guardado.

Las credenciales didácticas son:

| Campo | Valor |
|---|---|
| Usuario | `alumno` |
| Contraseña | `Taller2026!` |

No reutilices esta contraseña en cuentas reales.

## 14. Sesión y autorización

Después de autenticar correctamente:

```python
session.clear()
session["user_id"] = user["id"]
```

La sesión conserva el identificador, no la contraseña. Antes de cada solicitud, la aplicación utiliza ese identificador para cargar `g.current_user`.

El decorador terminado comprueba que exista un usuario:

```python
def login_required(view_function):
    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        if not g.get("current_user"):
            return redirect(url_for("auth.login"))
        return view_function(*args, **kwargs)

    return wrapped_view
```

Se aplica a las rutas protegidas:

```python
@products_bp.get("")
@login_required
def list_products_view():
    ...
```

Cerrar sesión elimina la identidad conservada:

```python
session.clear()
```

Este ejercicio no incluye recuperación de contraseña, autenticación multifactor, bloqueo de intentos ni permisos complejos.

## 15. Productos almacenados en memoria

Cada producto se representa mediante un diccionario:

```python
{
    "id": 1,
    "name": "Tarjeta gráfica Nova RTX 4060 8 GB",
    "category": "Componentes",
    "subcategory": "Tarjetas gráficas",
    "description": "GPU para juego y creación de contenido.",
    "price": Decimal("6999.00"),
    "stock_quantity": 8,
}
```

El catálogo es una lista de 20 diccionarios. `list_products()` devuelve copias para evitar modificaciones accidentales desde la plantilla.

`Decimal` representa importes con precisión decimal. Un `float` puede introducir aproximaciones binarias no deseadas.

Los datos viven en el proceso de Python:

- se conservan mientras Flask continúa ejecutándose;
- un producto nuevo es visible en solicitudes posteriores;
- al reiniciar Flask se reconstruyen los 20 registros iniciales;
- todavía no existe almacenamiento compartido o persistente.

## 16. Registrar un producto

La ruta terminada conecta el formulario validado con `add_product`:

```python
if form.validate_on_submit():
    product = add_product(
        name=form.name.data,
        category=form.category.data,
        subcategory=form.subcategory.data,
        description=form.description.data,
        price=form.price.data,
        stock_quantity=form.stock_quantity.data,
    )
    flash(
        f"Producto #{product['id']} registrado correctamente.",
        "success",
    )
    return redirect(
        url_for("products.list_products_view")
    )
```

`add_product`:

1. calcula el siguiente identificador;
2. limpia espacios sobrantes;
3. normaliza el precio a dos decimales;
4. agrega el diccionario a la lista;
5. devuelve una copia del nuevo producto.

El primer producto agregado después de los 20 iniciales recibe el identificador 21.

## 17. Patrón Post/Redirect/Get

Después de registrar correctamente se utiliza esta secuencia:

```text
POST /products/new
        ↓
Validar y registrar
        ↓
Redirigir a /products
        ↓
GET /products
```

La redirección reduce la posibilidad de repetir el registro al actualizar el navegador.

## 18. Configuración y secretos

`.env.example` documenta los nombres de las variables y puede publicarse. `.env` contiene valores locales y no debe registrarse en Git.

| Variable | Uso |
|---|---|
| `SECRET_KEY` | Firma la sesión y los tokens CSRF |
| `FLASK_DEBUG` | Controla funciones de desarrollo local |
| `HOST` | Dirección en la que escucha Flask |
| `PORT` | Puerto local; inicialmente 5001 |
| `DATA_MODE` | `memory` en la primera sesión |
| `DATABASE_URL` | Conexión que se utilizará con PostgreSQL |

La clave incluida en `.env.example` sólo sirve como valor de desarrollo. No debe utilizarse en producción.

## 19. Registrar los cambios con Git

La mini actividad puede conservarse en un commit independiente:

```bash
git add app/info app/templates/info/index.html app/__init__.py
git diff --staged
git commit -m "Agrega módulo informativo con blueprint"
```

Después de completar login y productos:

```bash
git add app/auth/store.py app/auth/routes.py app/products/routes.py
git diff --staged
git commit -m "Completa login y catálogo en memoria"
```

Después de mostrar **Agotado** en la plantilla:

```bash
git add app/templates/products/list.html
git diff --staged
git commit -m "Muestra productos agotados en el catálogo"
```

Antes de cada commit utiliza `git status`, `git diff` y `git diff --staged`. No agregues `.env`, `.venv`, `__pycache__`, contraseñas ni tokens.

## 20. Diagnóstico básico

### `/info` muestra 404

Comprueba que `info_bp` esté importado y registrado en `create_app`.

### Flask no encuentra `info/index.html`

La ruta exacta debe ser:

```text
app/templates/info/index.html
```

### El catálogo aparece vacío

Comprueba que `list_products_view` entregue `list_products()` y no `[]`.

### El login siempre se rechaza

Comprueba que `authenticate` normalice el nombre, busque una cuenta activa y utilice `check_password_hash`.

### La sesión no permanece

Comprueba que se asigne `session["user_id"]` y que `SECRET_KEY` tenga un valor estable durante la ejecución.

### El formulario rechaza la existencia cero

Comprueba que `stock_quantity` utilice `InputRequired` y `NumberRange(min=0)`.

### El producto desaparece al reiniciar

Es el comportamiento esperado mientras `DATA_MODE=memory`.

## 21. Sesiones posteriores

En la siguiente etapa se mantendrá el dominio, pero cambiará el almacenamiento:

```text
Sesión 1
Lista de diccionarios en memoria
        ↓
Sesión posterior
Modelos SQLAlchemy
        ↓
PostgreSQL en Docker Compose
```

Los conceptos de ruta, formulario, validación y plantilla continuarán siendo útiles. Cambiará principalmente la forma de consultar y guardar usuarios y productos.

La lógica de venta será una práctica posterior y no está resuelta en el proyecto base.

## 22. Comprobación personal

Responde sin consultar el código:

1. ¿Qué función crea la aplicación Flask?
2. ¿Por qué un blueprint debe registrarse?
3. ¿Qué elementos permiten que `/info` muestre HTML?
4. ¿Qué diferencia existe entre una ruta y una plantilla?
5. ¿Qué hace `form.validate_on_submit()`?
6. ¿Por qué la existencia utiliza `InputRequired`?
7. ¿Qué dato conserva la sesión?
8. ¿Por qué la contraseña no se guarda directamente?
9. ¿Dónde viven los productos durante la primera sesión?
10. ¿Por qué desaparece el producto 21 al reiniciar?
11. ¿Qué responsabilidad tendrá PostgreSQL?
12. ¿Qué archivos corresponden a cada uno de los tres commits sugeridos?

## 23. Materiales relacionados

- [Preparación del entorno](preparacion_entorno.md).
- [Guía rápida de Linux](guia_rapida_linux.md).
- [Lista de comprobación previa](lista_comprobacion_previa.md).
- [README principal](../README.md).

