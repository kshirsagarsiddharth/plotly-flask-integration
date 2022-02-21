
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
from flask_dir import app, flask_app, app2

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
















df_box = px.data.tips()




layout2 = html.Div([
    html.P('x-axis:'),
    html.Div(
    dbc.Checklist(
        id = 'x-axis',
        options = [
            {'label':x,'value':x} for x in ['smoker','day','time','sex']
        ],
        value = ['time'],
       inline = True,
       switch = True
    ), className = 'form-check'),
    html.P('y-axis:'),
    dbc.RadioItems(
        id = 'y-axis',
        options = [
            {'label':y,'value':y} for y in ['total_bill','tip','size']
        ],
        value = 'tip',
        inline = True

    ),
    dcc.Graph(id = 'graph-id')
],
className = 'container'
)

@app2.callback(Output('graph-id', 'figure'),[Input('x-axis', 'value'), Input('y-axis', 'value')])
def generate_boxplot(x_value, y_value):
    print(x_value,y_value)
    return px.box(df_box,x = x_value,y=y_value, title='TIPS COMPARISION', template='presentation', color_discrete_sequence=px.colors.qualitative.D3)



