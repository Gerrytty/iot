import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import random
import plotly.graph_objs as go

ARR_SIZE = 200
MAX_Y = 100

c = 0
val_y = 0

app = dash.Dash(__name__)

@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')],
)
def update_graph_scatter(n):
    global yy
    global c
    global val_y

    if len(X) >= ARR_SIZE:
        X[c] = c
        Y[c] = random.randint(0, MAX_Y)
        c += 1
        if c == ARR_SIZE - 1:
            c = 0
    else:
        X.append(X[-1] + 1)
        Y.append(val_y)
        if len(X) < ARR_SIZE / 2:
            val_y += 1
        else:
            val_y -= 1

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers',
    )

    return {'data': [data],
            'layout': go.Layout(xaxis=dict(range=[0, ARR_SIZE]), yaxis=dict(range=[0, MAX_Y]), )}


if __name__ == '__main__':
    X = [0]
    Y = [0]

    app.layout = html.Div(
        [
            dcc.Graph(id='live-graph', animate=False),
            dcc.Interval(
                id='graph-update',
                interval=100,
            ),
        ]
    )

    app.run_server(host="192.168.1.74", port=8080)
