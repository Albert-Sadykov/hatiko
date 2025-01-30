from flask import Flask
from app.api.imei_api import api as imei_api_blueprint

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(imei_api_blueprint)
    
    return app