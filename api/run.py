import os

from flask import Flask, jsonify
from dotenv import load_dotenv

from config import Config
from database import db
from models import Artist, Album, Genre, Track  # noqa: F401 (imported for metadata)
from routes import register_routes


def create_app() -> Flask:
    # Load environment variables from .env when running locally
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Simple health check endpoint
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    # Register all CRUD routes
    register_routes(app)

    return app


app = create_app()

if __name__ == "__main__":
    # 0.0.0.0 so it works inside Docker; 8000 is the exposed port
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=False)
