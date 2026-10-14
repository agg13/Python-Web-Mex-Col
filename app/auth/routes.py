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
        if not g.get("current_user"):
            flash("Inicia sesión para acceder a esta página.", "warning")
            return redirect(url_for("auth.login", next=request.path))
        return view_function(*args, **kwargs)

    return wrapped_view


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if g.get("current_user"):
        return redirect(url_for("products.list_products_view"))

    form = LoginForm()
    if form.validate_on_submit():
        user = authenticate(form.username.data, form.password.data)
        if user:
            session.clear()
            # TODO SESIÓN 2: los modelos utilizan atributos en lugar de llaves.
            session["user_id"] = user["id"]
            flash(f"Bienvenido, {user['username']}.", "success")
            return redirect(url_for("products.list_products_view"))
        flash("El usuario o la contraseña no son válidos.", "danger")

    return render_template("auth/login.html", form=form)


@auth_bp.post("/logout")
@login_required
def logout():
    session.clear()
    flash("La sesión se cerró correctamente.", "info")
    return redirect(url_for("auth.login"))
