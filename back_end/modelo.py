from config import *

class Livro(db.Model):

    nome = db.Column(db.String(254), primary_key=True)
    autor = db.Column(db.String(254))
    ano = db.Column(db.String(254))
    
    def __str__(self):
        return self.nome + ", " + self.autor + ", " + self.ano

    def json(self):
        return ({
            "nome": self.nome,
            "autor": self.autor,
            "ano": self.ano,
        })