import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))  # Diretório raiz

connex_app = connexion.App(__name__, specification_dir=basedir)  # Cria o Objeto Connexion

app = connex_app.app

sqlite_url = "sqlite:///" + os.path.join(basedir, "products.db")  # Conecta ao banco SQLite

# # # Configura o banco SQLite no App Connexion
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
