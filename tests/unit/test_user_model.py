import pytest
from datetime import datetime
from app.models.user import User

def test_new_user():
    """Test crear un nuevo usuario."""
    user = User(
        name='Test User',
        email='test@example.com'
    )
    
    assert user.name == 'Test User'
    assert user.email == 'test@example.com'
    assert user.id is None
    assert isinstance(user.created_at, datetime)
    assert isinstance(user.updated_at, datetime)

def test_user_repr():
    """Test la representación en string del usuario."""
    user = User(
        name='Test User',
        email='test@example.com'
    )
    
    assert str(user) == '<User Test User>'

def test_user_to_dict():
    """Test la conversión del usuario a diccionario."""
    user = User(
        name='Test User',
        email='test@example.com'
    )
    
    user_dict = user.to_dict()
    
    assert user_dict['name'] == 'Test User'
    assert user_dict['email'] == 'test@example.com'
    assert 'id' in user_dict
    assert 'created_at' in user_dict
    assert 'updated_at' in user_dict
    assert isinstance(user_dict['created_at'], str)
    assert isinstance(user_dict['updated_at'], str) 