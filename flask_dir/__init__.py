import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import Flask



#app = dash.Dash()

flask_app = Flask(__name__)
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],url_base_pathname='/external_dashboard/', server = flask_app)
app2 = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],url_base_pathname='/external_dashboard_two/', server = flask_app)
flask_app.config['SECRET_KEY'] = '8eb99d7900a98f5a894761e61d5076dd'
flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(flask_app)
bcrypt = Bcrypt(flask_app)
login_manager = LoginManager(flask_app)

from flask_dir import routes
