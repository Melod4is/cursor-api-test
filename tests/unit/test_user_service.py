import pytest
from app import create_app
from app.models.user import User
from app.models.base import db
from app.services.user_service import UserService

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user(session):
    """Test crear un usuario usando el servicio."""
    user_data = {
        'name': 'Test User',
        'email': 'test@example.com'
    }
    
    user = UserService.create_user(user_data)
    
    assert user['name'] == user_data['name']
    assert user['email'] == user_data['email']
    assert 'id' in user
    assert 'created_at' in user

def test_get_user(session):
    """Test obtener un usuario por ID."""
    # Crear un usuario de prueba
    user = User(name='Test User', email='test@example.com')
    session.add(user)
    session.commit()
    
    # Obtener el usuario usando el servicio
    result = UserService.get_user_by_id(user.id)
    
    assert result['name'] == user.name
    assert result['email'] == user.email
    assert result['id'] == user.id

def test_get_all_users(session):
    """Test obtener todos los usuarios."""
    # Crear usuarios de prueba
    users = [
        User(name='User 1', email='user1@example.com'),
        User(name='User 2', email='user2@example.com')
    ]
    session.add_all(users)
    session.commit()
    
    # Obtener todos los usuarios usando el servicio
    result = UserService.get_all_users()
    
    assert len(result) == 2
    assert result[0]['name'] == users[0].name
    assert result[1]['name'] == users[1].name

def test_update_user(session):
    """Test actualizar un usuario."""
    # Crear un usuario de prueba
    user = User(name='Test User', email='test@example.com')
    session.add(user)
    session.commit()
    
    # Actualizar el usuario
    update_data = {'name': 'Updated Name'}
    result = UserService.update_user(user.id, update_data)
    
    assert result['name'] == 'Updated Name'
    assert result['email'] == user.email

def test_delete_user(session):
    """Test eliminar un usuario."""
    # Crear un usuario de prueba
    user = User(name='Test User', email='test@example.com')
    session.add(user)
    session.commit()
    
    # Eliminar el usuario
    UserService.delete_user(user.id)
    
    # Verificar que el usuario fue eliminado
    result = UserService.get_user_by_id(user.id)
    assert result is None 