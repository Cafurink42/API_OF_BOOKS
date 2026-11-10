from flask_restx import Namespace, Resource, fields

from ..extensions import db
from ..models import Livro
from .auth import requer_api_key


ns = Namespace("livros", description="Operações com livros")

campos_livro = {
    "titulo":fields.String(
        required=True, 
        min_length=1, 
        max_lenght=150,
        description="Titulo do livro", 
        example="Dom Casmurro"),
    "author":fields.String(
        required=True, 
        min_lenght=1,
        max_lenght=100,
        description="Nome do autor",
        example="Machado de Assis",
    ),
    "ano_publicacao":fields.Integer(
        min=0, description="Ano de publicação", 
        example=1899
    ),
    "isbn":fields.Integer(
     max_length=20, 
     description= "ISBN único",
     example="9788525406958"),
}

# Entrada (POST/PUT): strict=True rejeita campos desconhecidos com erro 400
livro_entrada = ns.model("LivroEntrada", campos_livro, strict=True)

# Entrada parcial (PATCH): mesmos campos, mas nenhum é obrigatório
livro_parcial = ns.model("LivroParcial", {
"titulo": fields.String(min_length=1, max_length=150),
"autor": fields.String(min_length=1, max_length=100),
"ano_publicacao": fields.Integer(min=0),
"isbn": fields.String(max_length=20),
}, strict=True)

# Saída: campos do livro + os gerados pelo servidor (somente leitura)
livro_saida = ns.model("Livro", {
**campos_livro,
"id": fields.Integer(readonly=True, description="Identificador"),
"criado_em": fields.DateTime(readonly=True, description="Data de criação"),
})

livros_paginados = ns.model("LivrosPaginados", {
"items": fields.List(fields.Nested(livro_saida)),
"page": fields.Integer(description="Página atual"),
"per_page": fields.Integer(description="Itens por página"),
"total": fields.Integer(description="Total de registros"),
"pages": fields.Integer(description="Total de páginas"),
})