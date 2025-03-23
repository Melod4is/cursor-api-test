# API Flask de Ejemplo

Este es un proyecto de ejemplo que muestra una estructura robusta de una API REST con Flask, incluyendo pruebas unitarias y una arquitectura modular.

## Estructura del Proyecto

```
.
├── app/                    # Módulo principal de la aplicación
│   ├── __init__.py        # Inicialización de la aplicación
│   ├── config.py          # Configuración de la aplicación
│   ├── api/               # Rutas y endpoints
│   │   └── users.py       # Rutas de usuarios
│   ├── models/            # Modelos de la base de datos
│   │   ├── base.py       # Configuración base de SQLAlchemy
│   │   └── user.py       # Modelo de usuario
│   ├── schemas/           # Esquemas de validación
│   │   └── user.py       # Esquema de usuario
│   └── services/          # Lógica de negocio
│       └── user_service.py # Servicio de usuarios
├── tests/                 # Pruebas
│   ├── unit/             # Pruebas unitarias
│   │   └── test_user_service.py
│   └── integration/      # Pruebas de integración
├── app.py                # Punto de entrada de la aplicación
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Este archivo
```

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Crear archivo .env:
```
SECRET_KEY=tu-clave-secreta
DATABASE_URL=sqlite:///app.db
```

## Uso

1. Iniciar la aplicación:
```bash
python app.py
```

2. La API estará disponible en `http://localhost:5000`

## Endpoints Disponibles

- GET `/api/users`: Obtener todos los usuarios
- GET `/api/users/<id>`: Obtener un usuario específico
- POST `/api/users`: Crear un nuevo usuario
- PUT `/api/users/<id>`: Actualizar un usuario
- DELETE `/api/users/<id>`: Eliminar un usuario

## Pruebas

Para ejecutar las pruebas:

```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar pruebas con cobertura
pytest --cov=app tests/

# Ejecutar pruebas específicas
pytest tests/unit/test_user_service.py
```

## Características

- Arquitectura modular y escalable
- Separación de responsabilidades (MVC)
- Validación de datos con Marshmallow
- Pruebas unitarias y de integración
- Configuración por entorno (desarrollo, pruebas, producción)
- Documentación de API
- Manejo de errores
