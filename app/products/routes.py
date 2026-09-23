from flask import Blueprint, flash, redirect, render_template, url_for

from app.auth.routes import login_required
from .forms import ProductForm
from .store import add_product, list_products


products_bp = Blueprint("products", __name__, url_prefix="/products")


@products_bp.get("")
@login_required
def list_products_view():
    # TODO SESIÓN 1: sustituir la lista vacía por list_products().
    return render_template(
        "products/list.html",
        products=[],
    )


@products_bp.route("/new", methods=["GET", "POST"])
@login_required
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        # TODO SESIÓN 1:
        # 1. Enviar los datos validados a add_product.
        # 2. Mostrar el identificador generado.
        # 3. Redirigir al catálogo.
        _ = add_product, list_products, redirect, url_for
        flash("La lógica de registro se completará durante la sesión.", "warning")

    return render_template("products/new.html", form=form)
