from decimal import Decimal

from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange


class ProductForm(FlaskForm):
    name = StringField(
        "Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(
                min=3,
                max=120,
                message="El nombre debe tener entre 3 y 120 caracteres.",
            ),
        ],
    )
    category = SelectField(
        "Categoría",
        choices=[("Componentes", "Componentes"), ("Equipos", "Equipos")],
        validators=[DataRequired(message="La categoría es obligatoria.")],
    )
    subcategory = StringField(
        "Subcategoría",
        validators=[
            DataRequired(message="La subcategoría es obligatoria."),
            Length(
                min=3,
                max=80,
                message="La subcategoría debe tener entre 3 y 80 caracteres.",
            ),
        ],
    )
    description = TextAreaField(
        "Descripción",
        validators=[
            DataRequired(message="La descripción es obligatoria."),
            Length(
                min=10,
                max=500,
                message="La descripción debe tener entre 10 y 500 caracteres.",
            ),
        ],
    )
    price = DecimalField(
        "Precio",
        places=2,
        rounding=None,
        validators=[
            InputRequired(message="El precio es obligatorio."),
            NumberRange(
                min=Decimal("0.01"),
                message="El precio debe ser de al menos 0.01.",
            ),
        ],
    )
    stock_quantity = IntegerField(
        "Cantidad en almacén",
        validators=[
            InputRequired(message="La cantidad en almacén es obligatoria."),
            NumberRange(min=0, message="La cantidad no puede ser negativa."),
        ],
    )
    submit = SubmitField("Registrar producto")
