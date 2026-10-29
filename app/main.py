# para activar = python -m uvicorn main:app --reload 
from fastapi import FastAPI
from api.v1.api import api_router



app = FastAPI(
    title="E-comerce API",
    description="""
        Api RESTful completa para la gestión E-comerce.

        Incluye:
        - Autenticación con Jwt
        - Administración de productos y categorias
        - Carrito de compras
        - Gestión de pedidos
""",

version="1.0.0",

contact={
    "name": "Andriy Dev - Equipo Backend",
    "url": "https://github.com/Andriy2406",
    "email": "jhostinguzman2006@gmail.com"
},

license_info={
    "name": "MIT License",
    "url": "https://opensource.org/licenses/MIT",
}
)


app.include_router(api_router, prefix="/api/v1")


