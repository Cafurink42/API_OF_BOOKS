import hmac 
from functools import wraps

from flask import current_app, request
from flask_restx import abort



def requer_api_key(func):
    """Exige o cabeçalho X-API-KEY nas rotas que modificam dados."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        recebida = request.headers.get("X-API-KEY", "")
        esperada = current_app.config["API_KEY"]
        if not hmac.compare_digest(recebida, esperada):
            abort (401, "Acesso não autorizado.")
        return func(*args, **kwargs)
    return wrapper
#Um decorator que exige o cabeçalho X-API-KEY nas rotas que criam, alteram ou removem dados.