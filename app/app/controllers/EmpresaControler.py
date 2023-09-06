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
        "cnpj":request.form["cnpj"]
    }

    try:

        empresa = Empresa(empresa["titulo"], empresa["descricao"], empresa["endereco"], empresa["cnpj"])
        
        db.session.add(empresa)
        db.session.commit()
        
        return redirect("/", session = session)

    except Exception as e:  
        print(e)
        return redirect("/", session = session)

@app.route("/servicos/empresas")
def showEmpresa():
    
    servico = "empresas"
    consulta = Empresa.query.all()
    lista = []
    
    for i in consulta:
        lista.append(i.toJson())
        
    print(lista)    

    return render_template(f"resultPage.html", lista = lista, servico = servico)