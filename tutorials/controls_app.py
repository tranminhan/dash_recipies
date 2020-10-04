import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
  html.Label('Dropdown'),
  dcc.Dropdown(
    options=[
      {'label': 'New York City', 'value': 'NYC'},
      {'label': u'Montreál', 'value': 'MTL'},
      {'label': 'San Francisco', 'value': 'SF'}
    ]
  ),

  html.Label('Multi-Select Dropdown'),
  dcc.Dropdown(
    options=[
      {'label': 'New York City', 'value': 'NYC'},
      {'label': u'Montreál', 'value': 'MTL'},
      {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL', 'SF'],
    multi=True
  ),

  html.Label('Radio Items'),
  dcc.RadioItems(
    options=[
      {'label': 'New York City', 'value': 'NYC'},
      {'label': u'Montreál', 'value': 'MTL'},
      {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
  ),

  html.Label('Checkboxes'),
  dcc.Checklist(
    options=[
      {'label': 'New York City', 'value': 'NYC'},
      {'label': u'Montreál', 'value': 'MTL'},
      {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL', 'SF']
  ),

  html.Label('Input'),
  dcc.Input(value='MTL', type='text'),

  html.Label('Slider'),
  dcc.Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
    value=5,
  ),
], style={'columnCount': 4})



if __name__ == '__main__':
  app.run_server(debug=True)
