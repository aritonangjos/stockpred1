from flask import Flask


def create_app() -> Flask:
    """Application factory for the stock prediction dashboard."""
    app = Flask(__name__)

    from .routes import bp as main_bp

    app.register_blueprint(main_bp)
    return app
