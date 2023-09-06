from sqlalchemy import null
from sqlalchemy import or_
from app import app, db
from app.model.Empresa import Empresa
from app.model.ferramenta import Ferramenta
from app.model.PrestadorDeServico import PrestadorDeServico
from app.model.Usuario import Usuario
from app.connector import consultar
from flask import render_template, redirect, request, session


@app.route("/homepage")
@app.route('/')
def index():
    return render_template("index.html", session = session)

@app.route('/login')
def login():
    return render_template("index.html", session = session)

@app.route('/cadastro')
def cadastro():
    return render_template("form.html")

@app.route("/logout")
def logout():
    if "email" in session:
        del session["email"]
    return render_template("index.html", session=session)

@app.route('/usuarios/edit')
def edit():
    if "email" in session:
        return render_template("editarPerfil.html", session = session)
    return redirect("/cadastro", session = session)

@app.route("/edit/nome")
def editNome():
    return render_template("editNome.html", usuario = session)

@app.route("/edit/email")
def editEmail():
    return render_template("editEmail.html", usuario = session)

@app.route("/edit/senha")
def editSenha():
    return render_template("editSenha.html", usuario = session)

@app.route('/cadastrarFerramenta')
def cadastrarFerramentas():
    return render_template('cadastroDeFerramentas.html')
    
@app.route('/cadastrarEmpresa')
def cadastrarEmpresas():
    return render_template('cadastroDeEmpresas.html')

@app.route('/cadastrarPrestador')
def cadastrarPrestador():

    return render_template('cadastroDePrestadores.html')

    redirect("/homepage", session)
    
from app.controllers import UsuarioControler

from app.controllers import FerramentaControler

from app.controllers import EmpresaControler

from app.controllers import PrestadorDeServicoController


@app.route("/search", methods=["POST"])
def search():
    servico = "todos"
    busca = {
        "search":request.form["search"]
    }

    consulta = busca["search"]
    lista = []
    stringDeBusca = f'%{consulta}%'

    consultaEmpresa = Empresa.query.filter(or_(Empresa.titulo.like(stringDeBusca), Empresa.descricao.like(stringDeBusca))).all()
    consultaFerramenta = Ferramenta.query.filter(or_(Ferramenta.titulo.like(stringDeBusca), Ferramenta.descricao.like(stringDeBusca))).all()
    consultaPrestador = PrestadorDeServico.query.filter(or_(PrestadorDeServico.titulo.like(stringDeBusca), PrestadorDeServico.descricao.like(stringDeBusca))).all()
    for i in consultaEmpresa:
        lista.append(i.toJson())

    for i in consultaFerramenta:
        lista.append(i.toJson())

    for i in consultaPrestador:
        lista.append(i.toJson())  

    return render_template(f"resultPage.html", lista = lista, servico = servico, session = session)
    redirect("/" )