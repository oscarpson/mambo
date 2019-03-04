from flask import Flask
from blueprint import mambo_route as mambo


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    
   
   
    app.register_blueprint(mambo)

    return app
