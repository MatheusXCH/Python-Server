import json
import connexion

from flask import Flask, render_template, request

import config

# Carrega a aplicação do Connexion
connex_app = config.connex_app
connex_app.add_api("swagger.yml")  # Linka a aplicação com a API definida no swagger.yml


@connex_app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    connex_app.run(debug=True)
