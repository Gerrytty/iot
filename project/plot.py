import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import plotly.graph_objs as go

from consumer import SensorsUpdater

ARR_SIZE = 200
MAX_Y = 100

c = 0
val_y = 0
prev_size = 0

app = dash.Dash(__name__)
sensor_updater = SensorsUpdater("topic_1", ["localhost:9092"])
sensor_updater.endless_consume()

@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')],
)
def update_graph_scatter(n):
    global prev_size

    if prev_size != len(sensor_updater.arr_of_vals_of_sensor):
        print("New alement ploting...")

        global yy
        global c
        global val_y

        if len(X) >= ARR_SIZE:
            X[c] = c
            Y[c] = sensor_updater.arr_of_vals_of_sensor[prev_size]
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

        prev_size = len(sensor_updater.arr_of_vals_of_sensor)

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

    app.run_server(host="192.168.88.241", port=8080)