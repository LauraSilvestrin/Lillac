from app import db


class Usuario(db.Model):
    __tablename__ = "usuarios"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(50))
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
    def toJson(self):
        return {"id":self.id, "nome":self.nome, "email":self.email, "senha":self.senha}