# import json
# from pprint import pprint

# from flask import Flask, render_template, request
# from flask_socketio import SocketIO
# import connexion

# # # Flask and Flask_SocketIO initial setup
# app = Flask(__name__, template_folder="templates", static_folder="static")
# app.config["SECRET_KEY"] = "secret"
# socketio = SocketIO(app)

# clients = []  # # Persists all the current clients connected to the server
# products = []  # # Array to store the products (temporarily)


# # # Default web page
# @app.route("/")
# def home():
#     return render_template("home.html")


# # # Creating SocketIO events for when client connects to and disconnects from the server
# @socketio.event
# def connect():
#     print("Connected client: " + request.sid)
#     clients.append(request.sid)
#     socketio.start_background_task(task, request.sid)
#     socketio.emit("client_count", len(clients))


# @socketio.event
# def disconnect():
#     print("Disconnected client: " + request.sid)
#     clients.remove(request.sid)
#     socketio.emit("client_count", len(clients))


# def task(sid):
#     socketio.sleep(5)

#     # # Request data from the client and stores it in the products list
#     socketio.emit(
#         "create_product",
#         {"request": "put"},
#         callback=lambda json_response: (products.append(json_response), print(json.dumps(json_response, indent=4))),
#         to=sid,
#     )


# # # All Products API
# @app.route("/products", methods=["GET"])
# def all_products_page():
#     if request.method == "GET":
#         response = {"result": products}
#         return response
#     else:
#         return "Error 405 - Method Not Allowed"


# # # Products/<product_id> API
# @app.route("/products/<product_id>", methods=["GET", "POST", "DELETE"])
# def product_page(product_id):

#     if request.method == "POST":
#         data = request.get_json(force=True)
#         data["id"] = product_id
#         for product in products:
#             if data["id"] == product["id"]:
#                 return "Error - Already used ID"
#         products.append(data)
#         return {"success": True}

#     if request.method == "GET":
#         json_response = {"status": "failure"}
#         for product in products:
#             if int(product["id"]) == int(product_id):
#                 json_response.update({"status": "success", "data": product})
#                 socketio.emit(
#                     "get_product", product, callback=lambda json_response: print(json.dumps(json_response, indent=4))
#                 )
#         return json_response

#     if request.method == "DELETE":
#         json_response = {"status": "failure"}
#         for product in products:
#             if int(product["id"]) == int(product_id):
#                 products.remove(product)
#                 json_response = {"status": "success", "data": product}
#         return json_response

#     else:
#         return "Error 405 - Method Not Allowed"


# if __name__ == "__main__":
#     socketio.run(app, debug=True)
