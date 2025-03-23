import pytest
from app.models.user import User

def test_get_users(client, session):
    """Test obtener todos los usuarios a través de la API."""
    # Crear usuarios de prueba
    users = [
        User(name='User 1', email='user1@example.com'),
        User(name='User 2', email='user2@example.com')
    ]
    session.add_all(users)
    session.commit()
    
    # Hacer la petición GET
    response = client.get('/api/users')
    
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]['name'] == users[0].name
    assert data[1]['name'] == users[1].name

def test_get_user(client, session):
    """Test obtener un usuario específico a través de la API."""
    # Crear un usuario de prueba
    user = User(name='Test User', email='test@example.com')
    session.add(user)
    session.commit()
    
    # Hacer la petición GET
    response = client.get(f'/api/users/{user.id}')
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == user.name
    assert data['email'] == user.email

def test_create_user(client):
    """Test crear un usuario a través de la API."""
    user_data = {
        'name': 'New User',
        'email': 'new@example.com'
    }
    
    # Hacer la petición POST
    response = client.post('/api/users', json=user_data)
    
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == user_data['name']
    assert data['email'] == user_data['email']

def test_update_user(client, session):
    """Test actualizar un usuario a través de la API."""
    # Crear un usuario de prueba
    user = User(name='Test User', email='test@example.com')
    session.add(user)
    session.commit()
    
    update_data = {'name': 'Updated Name'}
    
    # Hacer la petición PUT
    response = client.put(f'/api/users/{user.id}', json=update_data)
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == update_data['name']
    assert data['email'] == user.email

def test_delete_user(client, session):
    """Test eliminar un usuario a través de la API."""
    # Crear un usuario de prueba
    user = User(name='Test User', email='test@example.com')
    session.add(user)
    session.commit()
    
    # Hacer la petición DELETE
    response = client.delete(f'/api/users/{user.id}')
    
    assert response.status_code == 204
    
    # Verificar que el usuario fue eliminado
    response = client.get(f'/api/users/{user.id}')
    assert response.status_code == 404 