from flask import request, redirect, render_template, session
from app import app
from app import db

from app.model.ferramenta import Ferramenta

@app.route("/cadastro/ferramenta/", methods=["POST"])
def createFerramenta():

    tecnologiasAssistivas = {
        "titulo":request.form["titulo"],
        "descricao":request.form["descricao"],
        "link":request.form["link"],
        "empresa":request.form["empresa"]
        
    }

    try:

        tecnologiasAssistivas = Ferramenta(tecnologiasAssistivas["titulo"], tecnologiasAssistivas["descricao"], tecnologiasAssistivas["link"], tecnologiasAssistivas["empresa"])
        
        db.session.add(tecnologiasAssistivas)
        db.session.commit()
        
        return redirect("/", session = session)

    except Exception as e:  
        print(e)
        return redirect("/", session = session)

@app.route("/servicos/tecnologias")
def showFerramenta():
    
    servico = "ferramentas"
    consulta = Ferramenta.query.all()
    lista = []
    
    for i in consulta:
        lista.append(i.toJson())
        
    print(lista)    

    return render_template(f"resultPage.html", lista = lista, servico = servico)


