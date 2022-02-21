import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px


#app = dash.Dash()
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],url_base_pathname='/external_dashboard/')

flask_app = app.server

from flask_dir import routes
