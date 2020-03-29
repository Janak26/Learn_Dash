import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
	html.Label('Choose a city'),
	dcc.Dropdown(
		id = 'first-dropdown',
		options = [

		{'label':'Mumbai', 'value':'MUM'},
		{'label':'New Delhi', 'value':'DEL'},
		{'label':'Bengaluru', 'value':'BEN', 'disabled':True }
		],
		placeholder = 'Select your city',
		# disabled = True
		# value='DEL',
		# multi = True
		),

	html.Br(),
	html.Label('Simple slider exapmpe'),
	dcc.Slider(
		min = 1,
		max = 10,
		value = 3,
		step = 0.25,
		marks = {i:i for i in range(10)}
		),


	html.Br(),
	html.Label('Simple Range SLider'),
	dcc.RangeSlider(
		min = 1,
		max = 10,
		step = 0.25,
		value = [1.75, 5.50],
		marks = {i:i for i in range(10)}
		),

	html.Br(),
	html.Label('Sample Input box'),
	dcc.Input(
		placeholder = 'Enter your name',
		type = 'text',
		value = ''),


	html.Br(),
	html.Br(),
	dcc.Textarea(
		placeholder = 'Enter any text',
		# value = 'Enter your placeholder',
		style = {'width':'100%', 'height':'50%'}),




	])


if __name__ == '__main__':
	app.run_server(port = 4050)