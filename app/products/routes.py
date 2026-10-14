from flask import Blueprint, flash, redirect, render_template, url_for

from app.auth.routes import login_required
from .forms import ProductForm
from .store import add_product, list_products


products_bp = Blueprint("products", __name__, url_prefix="/products")


@products_bp.get("")
@login_required
def list_products_view():
    return render_template(
        "products/list.html",
        products=list_products(),
    )


@products_bp.route("/new", methods=["GET", "POST"])
@login_required
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = add_product(
            name=form.name.data,
            category=form.category.data,
            subcategory=form.subcategory.data,
            description=form.description.data,
            price=form.price.data,
            stock_quantity=form.stock_quantity.data,
        )
        # TODO SESIÓN 2: acceder a product.id cuando Product sea un modelo.
        flash(f"Producto #{product['id']} registrado correctamente.", "success")
        return redirect(url_for("products.list_products_view"))

    return render_template("products/new.html", form=form)
