from flask import Blueprint, render_template


info_bp = Blueprint("info", __name__, url_prefix="/info")


@info_bp.get("")
def index():
    """Muestra una página informativa creada durante el taller."""

    return render_template("info/index.html")
