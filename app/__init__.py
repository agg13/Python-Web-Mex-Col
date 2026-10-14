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

    # TODO SESIÓN 2: después de definir User y Product, inicializar la
    # extensión, crear las tablas y ejecutar seed_database cuando
    # AUTO_INIT_DB sea verdadero.
    if app.config["DATA_MODE"] == "database":
        db.init_app(app)

    from .main.routes import main_bp
    from .auth.routes import auth_bp
    from .info.routes import info_bp
    from .products.routes import products_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(info_bp)
    app.register_blueprint(products_bp)

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
