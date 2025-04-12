"This is a simple application file to be run with Dash library"

from dash import Dash, html, dcc, callback, Output, Input
# import plotly.express as px
# import pandas as pd
import visualize

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = [
    html.H1(children='Sudoku Solver App', style={'textAlign':'center'}),
    html.Div([
        dcc.Upload(html.Button('Upload File'), id='upload_puzzle')
    ]),
    dcc.Graph(id='plot')
]

@app.callback(
    Output('plot', 'figure'),
    Input('upload_puzzle', 'puzzle')
    # State('upload_puzzle', 'filename')
)
def show_problem(puzzle):
    figure = visualize.visualize_sudoku(puzzle)
    print("It got here")
    return figure

if __name__ == '__main__':
    app.run(debug=True)