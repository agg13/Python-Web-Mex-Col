from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        "Usuario",
        validators=[
            DataRequired(message="El usuario es obligatorio."),
            Length(
                min=3,
                max=50,
                message="El usuario debe tener entre 3 y 50 caracteres.",
            ),
        ],
    )
    password = PasswordField(
        "Contraseña",
        validators=[
            DataRequired(message="La contraseña es obligatoria."),
            Length(
                min=8,
                max=128,
                message="La contraseña debe tener entre 8 y 128 caracteres.",
            ),
        ],
    )
    submit = SubmitField("Iniciar sesión")
