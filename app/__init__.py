from flask import Flask
from app.config import config
from app.models.base import db
from app.api.users import users_bp

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inicializar la base de datos
    db.init_app(app)
    
    # Registrar blueprints
    app.register_blueprint(users_bp, url_prefix='/api')
    
    # Crear tablas
    with app.app_context():
        db.create_all()
    
    return app 