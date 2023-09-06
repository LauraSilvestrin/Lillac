from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

# import pymysql
# pymysql.install_as_MySQLdb()

app = Flask(__name__)

# mysql://root:abrl0404@127.0.0.1/projeto #PC do Gabriel
# mysql://aulaBD@localhost/projeto #PC lab de baixo
#mysql://root:ifpr@localhost/projeto #lab de cima

# <Nome do SGBD>://<Usuário>:<Senha>@<Endereço>/<Nome do banco>

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@127.0.0.1/lillac"
app.secret_key = "q4t7w!z%C*F-JaNd"

db = SQLAlchemy(app)

from app.controllers import routes
