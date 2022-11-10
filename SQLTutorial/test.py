# import dash
# import pandas as pd
# from dash import dcc
# from dash import html
# from dash import Output, Input
# import plotly.express as px

####################dash line chart########################
# df = px.data.gapminder()
# all_continents = df.continent.unique()
#
# app = dash.Dash(__name__)
#
# app.layout = html.Div([dcc.Checklist(id='checklist', options=[{'label': x, 'value': x} for x in all_continents],
#                                      value=all_continents, labelStyle={'display': 'inline-block'}),
#                        dcc.Graph(id='line-chart'), ])
#
#
# @app.callback(Output('line-chart', 'figure'), [Input('checklist', 'value')])
# def update_line_chart(continents):
#     mask = df.continent.isin(continents)
#     fig = px.line(df[mask], x='year', y='lifeExp', color='country')
#     return fig


# app.run_server(debug=True)

####################dash bar chart########################
# df = px.data.tips()
# days = df.day.unique()
#
# app = dash.Dash(__name__)
#
# app.layout = html.Div([
#     dcc.Dropdown(
#         id="dropdown",
#         options=[{"label": x, "value": x} for x in days],
#         value=days[0],
#         clearable=False,
#     ),
#     dcc.Graph(id="bar-chart"),
# ])
#
#
# @app.callback(
#     Output("bar-chart", "figure"),
#     [Input("dropdown", "value")])
# def update_bar_chart(day):
#     mask = df["day"] == day
#     fig = px.bar(df[mask], x="sex", y="total_bill",
#                  color="smoker", barmode="group")
#     return fig
# app.run_server(debug=True)

####################dash pie chart########################
# df = px.data.tips()
# app = dash.Dash(__name__)
# app.layout = html.Div([html.P('Names'), dcc.Dropdown(id='weekdays', value='day',
#                                                      options=[{'label': x, 'value': x} for x in
#                                                               ['smoker', 'day', 'time', 'sex']],
#                                                      clearable=False),
#                        html.P('Values'), dcc.Dropdown(id='type', value='total_bill',
#                                                       options=[{'label': x, 'value': x} for x in
#                                                                ['total_bill', 'tip', 'size']],
#                                                       clearable=False),
#                        dcc.Graph(id='pie-chart')])
#
#
# @app.callback(Output('pie-chart', 'figure'), [Input('weekdays', 'value'),
#                                               Input('type', 'value')])
# def create_pie_chart(names, values):
#     fig = px.pie(df, names=names, values=values)
#     return fig
#
#
# app.run_server(debug=True)
# import pyodbc
# conx = pyodbc.connect('Driver = {SQL Server}; Server=CATERPILLAR; Database=AdventureWorks2014; Trusted_Connection=YES;')
# # conx = pyodbc.connect('Driver = {SQL Server}; Server = CATERPILLAR; Database=AdventureWorks2014; Trusted_Connection = yes;')
# # print(pyodbc.drivers())
# # conn = pyodbc.connect('Driver={SQL Server};'
# #                       'Server=CATERPILLAR;'
# #                       'Database=AdventureWorks2014;'
# #                       'Trusted_Connection=yes;')
# import sqlite3
# conn = sqlite3.connect()

import pandas as pd
import urllib.request
import ssl

url = 'https://www.investopedia.com/ask/answers/071414/whats-difference-between-moving-average-and-weighted-moving-average.asp'
context = ssl._create_unverified_context()
table = urllib.request.urlopen(url, context=context)
