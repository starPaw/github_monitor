from flask import Flask
from app.api import events, metrics


def create_app():
    app = Flask(__name__)
    app.register_blueprint(events.bp)
    app.register_blueprint(metrics.bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
