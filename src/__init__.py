import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

# SET ENV VARIABLE TO 
db_user     = os.getenv('MYSQL_USER')
db_pwd      = os.getenv('MYSQL_PASSWORD')
db_host     = os.getenv('MYSQL_HOST')
db_port     = os.getenv('MYSQL_PORT')
db_name     = os.getenv('MYSQL_DB')

DATABASE_URI = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)
db.create_all()
# bcrypt = Bcrypt(app)

from src import views

