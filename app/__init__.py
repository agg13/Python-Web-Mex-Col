import logging

from flask import Flask, g, render_template, session

from config import BaseConfig
from .auth.store import find_user_by_id
from .extensions import csrf, db


def create_app(config_object=BaseConfig):
    """Crea y configura una instancia de la aplicación."""

    app = Flask(__name__)
    app.config.from_object(config_object)

    csrf.init_app(app)

    # En la sesión 1 el catálogo vive en memoria. La extensión ya está
    # preparada y se activará al cambiar DATA_MODE en la sesión 2.
    if app.config["DATA_MODE"] == "database":
        db.init_app(app)

    from .main.routes import main_bp
    from .auth.routes import auth_bp
    from .products.routes import products_bp

    # MINI ACTIVIDAD GUIADA:
    # 1. Crear app/info/routes.py y definir info_bp.
    # 2. Importar aquí info_bp.
    # 3. Registrar el blueprint después de los módulos existentes.

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    # app.register_blueprint(info_bp)

    @app.before_request
    def load_current_user():
        user_id = session.get("user_id")
        g.current_user = find_user_by_id(user_id) if user_id else None

    @app.context_processor
    def inject_current_user():
        return {"current_user": g.get("current_user")}

    @app.errorhandler(404)
    def page_not_found(_error):
        return render_template("errors/404.html"), 404

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    return app
