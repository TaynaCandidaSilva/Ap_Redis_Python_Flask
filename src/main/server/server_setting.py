from flask import Flask  # type: ignore

from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliteConnectionHandler

redis_connection_handler = RedisConnectionHandler()
sqlite_connection_handler = SqliteConnectionHandler()

sqlite_connection_handler.connect()
redis_connection_handler.connect()

app = Flask(__name__)

from src.main.routes.products_routes import products_routes_bp

app.register_blueprint(products_routes_bp)
