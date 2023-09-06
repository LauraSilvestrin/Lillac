from app import db

class Empresa(db.Model):
    __tablename__ = "empresas"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String())
    descricao = db.Column(db.String())
    endereco = db.Column(db.String())
    cnpj = db.Column(db.String())


    def __init__(self, titulo, descricao, endereco, cnpj):
        self.titulo = titulo
        self.descricao = descricao
        self.endereco = endereco
        self.cnpj = cnpj


    def toJson(self):
        return {"id":self.id,
                "titulo":self.titulo,
                "descricao":self.descricao,
                "endereco":self.endereco,
                "cnpj":self.cnpj}


                

