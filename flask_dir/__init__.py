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



#app = dash.Dash()
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],url_base_pathname='/external_dashboard/')

flask_app = app.server
flask_app.config['SECRET_KEY'] = '8eb99d7900a98f5a894761e61d5076dd'
flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(flask_app)
bcrypt = Bcrypt(flask_app)
login_manager = LoginManager(flask_app)

from flask_dir import routes
