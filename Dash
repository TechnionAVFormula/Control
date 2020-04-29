

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from math import exp,tanh
from collections import deque
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

class Constants:

    ACTUAL_SPEED = "actual_speed"
    DESIRABLE_SPEED = "desirable_speed"
    ACTUAL_STEERING = "actual_steering"
    DESIRABLE_STEERING = "desirable_steering"
    POLYNOMIAL_A = "polynomial_a"
    POLYNOMIAL_B = "polynomial_b"
    POLYNOMIAL_C = "polynomial_c"
    TIME ="time"
    X = "x"
    Y = "y"
    ACCURACY = "accuracy"


class Dash:

    def __init__(self,state:{}):
        actual_speed = state[Constants.ACTUAL_SPEED]
        desirable_speed = state[Constants.DESIRABLE_SPEED]
        actual_steering = state[Constants.ACTUAL_STEERING]
        desirable_steering = state[Constants.DESIRABLE_STEERING]
        polynomial_a = state[Constants.POLYNOMIAL_A]
        polynomial_b = state[Constants.POLYNOMIAL_B]
        polynomial_c = state[Constants.POLYNOMIAL_C]
        time = state[Constants.TIME]


        x_const =[i for i in range(max(time)+10)]
        self.app = dash.Dash(__name__)

        # SPEED

        self.speed_fig =go.Figure()
        self.speed_fig.add_trace(go.Scatter(x=time,y=actual_speed, name="actual speed"))
        self.speed_fig.add_trace(go.Scatter(x=time,y=desirable_speed, name="desirable speed"))
        self.speed_fig.add_trace(go.Scatter(x=time,y=actual_speed, name="actual speed -kmh"))
        self.speed_fig.add_trace(go.Scatter(x=x_const,y=[30/3.6]*len(x_const),name="30-kmh"))
        self.speed_fig.add_trace(go.Scatter(x=x_const,y=[60/3.6]*len(x_const),name="60-kmh"))

        self.speed_fig.update_layout(
            xaxis_title = "Time[second]",
            yaxis_title = "Speed[meter/second]",
            xaxis = dict(range =[0,max(time)+10]),
            yaxis = dict(range =[0,100/3.6])
        )

        value =lambda x: x/(1+exp(-x))
        accuracy = lambda mona , machna : [abs(100-100*abs(tanh(((mona-machna)**2)//(machna+0.001)))) for mona, machna in zip(mona, machna)]
        self.speed_fig_data= go.Figure(
            data =[go.Table(header=dict(values=[Constants.TIME,Constants.ACTUAL_SPEED,Constants.DESIRABLE_SPEED,Constants.ACCURACY]),
                            cells = dict(values =[
                                         time,actual_speed,
                                         desirable_speed,
                                         accuracy(actual_speed, desirable_speed)]))])
        # STEERING

        self.steering_fig = go.Figure()
        self.steering_fig.add_trace(go.Scatter(x=time, y= actual_steering, name="actual steering",fillcolor="black"))
        self.steering_fig.add_trace(go.Scatter(x=time, y= desirable_steering, name="desirable steering"))

        self.steering_fig.update_layout(
            xaxis_title = "Time[Second]",
            yaxis_title = "Steering[Degree]",
            xaxis = dict(range=[0, max(time)+10]),
            yaxis = dict(range=[-40, 40])
        )

        self.steering_fig_data = go.Figure(
            data=[go.Table(header=dict(
                values=[Constants.TIME, Constants.ACTUAL_STEERING, Constants.DESIRABLE_STEERING, Constants.ACCURACY]),
                           cells=dict(values=[
                               time, actual_steering,
                               desirable_steering,
                               accuracy(actual_steering, desirable_steering)]))])




        # functions

        self.constrants_fig = go.Figure()
        self.constrants_fig.add_trace(go.Scatter(x=polynomial_a[Constants.X],
                                                 y=polynomial_a[Constants.Y],name = "polynomial a"))

        self.constrants_fig.add_trace(go.Scatter(x=polynomial_b[Constants.X],
                                                     y=polynomial_b[Constants.Y], name="polynomial b"))
        self.constrants_fig.add_trace(go.Scatter(x=polynomial_c[Constants.X],
                                                 y=polynomial_c[Constants.Y], name="polynomial c"))

        self.const_fig_data = go.Figure(
            data=[go.Table(header=dict(
                values=[Constants.POLYNOMIAL_A+"X",Constants.POLYNOMIAL_A+"Y", Constants.POLYNOMIAL_B+"X",
                        Constants.POLYNOMIAL_B+"Y" ,Constants.POLYNOMIAL_C+"X" , Constants.POLYNOMIAL_C+"Y"]),
                cells=dict(values=[
                               polynomial_a[Constants.X],
                               polynomial_a[Constants.Y],
                               polynomial_b[Constants.X],
                               polynomial_b[Constants.Y],
                               polynomial_c[Constants.X],
                               polynomial_c[Constants.Y]
                ]))])




        mins = lambda a, b, c: min(a, b, c)
        maxs = lambda a, b, c: max(a, b, c)
        min_ax = min(polynomial_a[Constants.X])
        min_ay = min(polynomial_a[Constants.Y])
        min_bx = min(polynomial_b[Constants.X])
        min_by = min(polynomial_b[Constants.Y])
        min_cx = min(polynomial_c[Constants.X])
        min_cy = min(polynomial_c[Constants.Y])
        max_ax = max(polynomial_a[Constants.X])
        max_ay = max(polynomial_a[Constants.Y])
        max_bx = max(polynomial_b[Constants.X])
        max_by = max(polynomial_b[Constants.Y])
        max_cx = max(polynomial_c[Constants.X])
        max_cy = max(polynomial_c[Constants.Y])

        min_gx =mins(min_ax,min_bx,min_cx)
        min_gy =mins(min_ay,min_by,min_cy)
        max_gx =maxs(max_ax,max_bx,max_cx)
        max_gy =maxs(max_ay,max_by,max_cy)

        self.constrants_fig.update_layout(
            xaxis_title="x value",
            yaxis_title="y value",

            xaxis=dict(range=[min_gx-10,max_gx+10]),
            yaxis=dict(range=[min_gy-10,max_gy+10])
        )

        self.app.layout = html.Div(children=[
            html.H1(children='Control'),

            html.Div(children='''Hello
            '''),
            dcc.Graph(
                id='speed graph',
                figure=self.speed_fig
            ),

            dcc.Graph(
                id ="data speed grath",
                figure=self.speed_fig_data
            ),

            dcc.Graph(
                id='streeing',
                figure=self.steering_fig
            ),
            dcc.Graph(
                id='data streeing',
                figure=self.steering_fig_data

            ),


            dcc.Graph(
                id='constrants',
                figure=self.constrants_fig
            ),
            dcc.Graph(
                id ="const fig data",
                figure =self.const_fig_data
            )

        ])



    def run(self):
        self.app.run_server(debug=True)


if __name__ == '__main__':

    dic = {
        Constants.ACTUAL_SPEED:[10,20,20,26],
        Constants.DESIRABLE_SPEED : [12,14,15,20] ,

        Constants.ACTUAL_STEERING :  [0,-5,5,10] ,
        Constants.DESIRABLE_STEERING : [0,-1,2,7 ] ,
        Constants.POLYNOMIAL_A : {
                    Constants.X: [1,2,3 ,4 ] ,
                    Constants.Y: [5, 3,6, 8]
        },
        Constants.POLYNOMIAL_B: {
            Constants.X: [2, 1, 9, 20],
            Constants.Y: [5, 3, 6, 8]
        },

        Constants.POLYNOMIAL_C: {
            Constants.X: [1, 4, 91, 45],
            Constants.Y: [1, 2, 8, 9]
        },

        Constants.TIME : [6,9,15,20]

    }
    my=Dash(dic)
    my.run()
