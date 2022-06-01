from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.config import PROD_DB

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = PROD_DB
db = SQLAlchemy(app)

from flaskblog import routes
