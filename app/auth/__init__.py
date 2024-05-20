from flask import Flask
from pymongo import MongoClient
from py2neo import Graph
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth.routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

def get_db():
    client = MongoClient(Config.MONGO_URI)
    return client.get_database()

def get_graph():
    graph = Graph(Config.NEO4J_URI, auth=(Config.NEO4J_USER, Config.NEO4J_PASSWORD))
    return graph
