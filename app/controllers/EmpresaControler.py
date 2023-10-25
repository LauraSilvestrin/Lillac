from flask import request, redirect, render_template, session
from app import app
from app import db

from app.model.Empresa import Empresa

@app.route("/cadastro/empresa/", methods=["POST"])
def createEmpresa():
    empresa = {
        "titulo":request.form["titulo"],
        "descricao":request.form["descricao"],
        "endereco":request.form["endereco"],
        "cnpj":request.form["cnpj"],
        "adm": 0
    }

    try:

        empresa = Empresa(empresa["titulo"], empresa["descricao"], empresa["endereco"], empresa["cnpj"], empresa["adm"])
        
        db.session.add(empresa)
        db.session.commit()
        
        return redirect("/")

    except Exception as e:  
        print(e)
        return redirect("/")

@app.route("/servicos/empresas")
def showEmpresa():
    
    servico = "empresas"
    consulta = Empresa.query.all()
    lista = []
    
    for i in consulta:
        adm = i.adm
        if adm == 1:
            lista.append(i.toJson())

    return render_template(f"resultPage.html", lista = lista, servico = servico)