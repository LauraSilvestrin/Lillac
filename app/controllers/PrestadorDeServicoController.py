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
        "descricao":request.form["descricao"],
        "adm": 0    
    }

    try:

        prestadorDeServico = PrestadorDeServico(prestador["titulo"], prestador["numero"], prestador["email"], prestador["descricao"], prestador["adm"])
        
        db.session.add(prestadorDeServico)
        db.session.commit()
        
        return redirect("/")

    except Exception as e:  
        print(e)
        return redirect("/addservice")


@app.route("/servicos/prestador")
def showPrestador():

    servico = "profissionais"
    consulta = PrestadorDeServico.query.all()
    lista = []
    
    for i in consulta:
        adm = i.adm
        if adm == 1:
            lista.append(i.toJson())
        

    return render_template(f"resultPage.html", lista = lista, servico = servico)