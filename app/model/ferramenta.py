from app import db

class Ferramenta(db.Model):
    __tablename__ = "tecnologiasassistivas"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String())
    descricao = db.Column(db.String())
    link = db.Column(db.String())
    empresaResponsavel = db.Column(db.String())
    adm = db.Column(db.Integer)
        
    def __init__(self, titulo, descricao, link, empresaResponsavel, adm):
        self.titulo = titulo
        self.descricao = descricao
        self.link = link
        self.empresaResponsavel = empresaResponsavel
        self.adm = adm

    
    def toJson(self):
        return {"id":self.id,
                "titulo":self.titulo,
                "descricao":self.descricao,
                "link":self.link,
                "empresaResponsavel":self.empresaResponsavel,
                "adm":self.adm}