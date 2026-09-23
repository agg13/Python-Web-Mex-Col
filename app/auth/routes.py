from functools import wraps

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from .forms import LoginForm
from .store import authenticate


auth_bp = Blueprint("auth", __name__)


def login_required(view_function):
    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        # TODO SESIÓN 1:
        # Verificar g.current_user y redirigir al login cuando no exista sesión.
        _ = g, request
        return view_function(*args, **kwargs)

    return wrapped_view


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # TODO SESIÓN 1:
    # Si ya existe g.current_user, redirigir directamente al catálogo.
    form = LoginForm()
    if form.validate_on_submit():
        # TODO SESIÓN 1:
        # 1. Autenticar las credenciales.
        # 2. Limpiar y crear la sesión con user_id.
        # 3. Mostrar confirmación y redirigir al catálogo.
        _ = authenticate, session, redirect, url_for
        flash("La lógica de autenticación se completará durante la sesión.", "warning")

    return render_template("auth/login.html", form=form)


@auth_bp.post("/logout")
@login_required
def logout():
    # TODO SESIÓN 1: limpiar la sesión antes de redirigir.
    flash("El cierre de sesión se completará durante la sesión.", "warning")
    return redirect(url_for("auth.login"))
