from flask import request, redirect, render_template, session
from app import app
from app import db

from app.model.PrestadorDeServico import PrestadorDeServico


@app.route("/cadastro/prestador", methods=["POST"])
def createPrestador():

    prestador = {
        "titulo":request.form["titulo"],
        "numero":request.form["numero"],
        "email":request.form["email"],
        "descricao":request.form["descricao"]
        
    }

    try:

        prestadorDeServico = PrestadorDeServico(prestador["titulo"], prestador["numero"], prestador["email"], prestador["descricao"])
        
        db.session.add(prestadorDeServico)
        db.session.commit()
        
        return redirect("/", session = session)

    except Exception as e:  
        print(e)
        return redirect("/", session = session)


@app.route("/servicos/prestador")
def showPrestador():

    servico = "profissionais"
    consulta = PrestadorDeServico.query.all()
    lista = []
    
    for i in consulta:
        lista.append(i.toJson())
        
    print(lista)    

    return render_template(f"resultPage.html", lista = lista, servico = servico)