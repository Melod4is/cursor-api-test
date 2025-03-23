import pytest
from app import create_app
from app.models.base import db

@pytest.fixture(scope='session')
def app():
    """Crear y configurar una nueva instancia de la aplicación para cada sesión de prueba."""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    """Crear un nuevo cliente de prueba para cada función."""
    return app.test_client()

@pytest.fixture(scope='function')
def runner(app):
    """Crear un nuevo runner de CLI para cada función."""
    return app.test_cli_runner()

@pytest.fixture(scope='function')
def session(app):
    """Crear una nueva sesión de base de datos para cada función."""
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()
        options = dict(bind=connection, binds={})
        session = db.create_scoped_session(options=options)
        
        db.session = session
        
        yield session
        
        transaction.rollback()
        connection.close()
        session.remove() 