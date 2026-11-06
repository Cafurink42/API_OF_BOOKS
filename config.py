import os

class Config:
    SQLALCHEMY_DATA_URI = os.gateenv("DATABASE_URL", "sqlite:///livraria.db")
    API_KEY = os.getenv("API_KEY", "minha-chave-secreta")


    #Ajustes do Flask-RESTX

    RESTX_MASK_SWAGGER = False #remove o parâmetro X-Fields da documentação
    RESTX_ERROR_404_HELP = False #remove sugestões automáticas nos erros 404

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATA_URI = "sqlite:///:memory:"

    