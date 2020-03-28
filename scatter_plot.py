import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

np.random.seed(50)
x_rand = np.random.randint(1, 61, 60)
y_rand = np.random.randint(1, 61, 60)


data = pd.read_csv('D:/ML_Projects/dash_learn/data/kc_house_data.csv')

app.layout = html.Div([
	

	dcc.Graph(
		id = 'SampleScatter',
		figure = {
		'data' : [

		go.Scatter(
			x = data['sqft_lot'],
			y = data['price'],
			mode = 'markers')

		],

		'layout' : go.Layout(
			title = 'Scatterplot Sample',
			xaxis = {'title':'Lot size'},
			yaxis = {'title':'Price'},
			hovermode = 'closest')
		})


	])


if __name__ == '__main__':
	app.run_server(port = 4050)


# 3384 5348 6704 3112 