
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
from flask_dir import app, flask_app

df = pd.read_csv("flask_dir\plotlydash\mpg.csv")

features = df.columns

layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='x-axis',
            options=[{'label': x, 'value': x} for x in features],
            value='displacement'
        )
    ], className='p-2 w-25'),
    html.Div([
        dcc.Dropdown(
            id='y-axis',
            options=[{'label': y, 'value': y} for y in features],
            value='mpg'
        ),

    ], className='p-2 w-25'),
    dcc.Graph(id='figure-graphic')
],
    className='container p-5 mr-5'
)


@app.callback(Output('figure-graphic', 'figure'), [Input('x-axis', 'value'), Input('y-axis', 'value')])
def update_graph(x_axis_name, y_axis_name):
    fig = px.scatter(data_frame=df, x=x_axis_name, y=y_axis_name, hover_data=[
                     'name'], template='presentation', opacity=0.7)
    fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGray')))
    fig.update_layout(hovermode = 'closest')

    return fig 

# if __name__ == "__main__":
#     flask_app.run(debug=True)

