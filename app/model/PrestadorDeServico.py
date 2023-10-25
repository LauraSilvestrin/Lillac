from app import db

class PrestadorDeServico(db.Model):
    __tablename__ = "prestadoresdeservico"    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String())
    numero = db.Column(db.String())
    email = db.Column(db.String())
    descricao = db.Column(db.String())
    adm = db.Column(db.Integer)
    
    def __init__(self, titulo, numero, email, descricao, adm):
        self.titulo = titulo
        self.numero = numero
        self.email = email
        self.descricao = descricao
        self.adm = adm
        
    def toJson(self):
        return {"id":self.id,
                "titulo":self.titulo,
                "numero":self.numero,
                "email":self.email,
                "descricao":self.descricao,
                "adm":self.adm}

