import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()


app.layout = html.Div([
	html.H1('Hello'),
	html.Div('A para'),

	dcc.Graph(
		id = 'samplechart',
		figure = {
		'data' : [

		{'x':[1,3,5], 'y':[4,5,6], 'type':'bar', 'name': 'First'},
		{'x':[1,3,5], 'y':[4,5,6], 'type':'bar', 'name': 'Second'}

		],

		'layout': {'title':'Simple Bar Chart'}
		})


	])

if __name__ == '__main__':
	app.run_server(port = 4050)