import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

## Defining variables
temp = pd.read_csv('Coal_Naturalgas_Generation_Data.csv',parse_dates=['Month'])
hovertexts0 = []
hovertexts1 = []
for indx in range(len(temp.Month)):
     hovertexts0.append('({y})Thousand MegaWattHours'.format(y=temp.natural_gas_thousand_megawatthours[indx]))
     hovertexts1.append('({y})Thousand MegaWattHours'.format(y=temp.coal_thousand_megawatthours[indx]))
color1='darkred'
color2='orange'
mytitle='Coal & Naturalgas generation Data'
tabtitle='Coal & Gas Data'
myheading=''

## Setting up chart
trace0 = go.Scatter(x=temp.Month,y=temp.natural_gas_thousand_megawatthours,mode='lines',name='Natural gas',showlegend=True,hoverinfo='x+text',hovertext=hovertexts0)
trace1 = go.Scatter(x=temp.Month,y=temp.coal_thousand_megawatthours,mode='lines',name='Coal',hoverinfo='x+text',hovertext=hovertexts1)
data = [trace0,trace1]
layout = go.Layout(title = "Coal and Natural Gas Electricity Generation", xaxis = dict(title='Year',tickmode = 'linear',tick0 = 'M1Y2005',dtick = 'M12'), yaxis = dict(title ='Thousand Megawatthours',tickformat=',d'),hovermode="closest")
fig = go.Figure(data=data, layout=layout)


## Initiating the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

## Setting up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='NaturalGas_Vs_Coal',
        figure=fig
    )
    ]
)

if __name__ == '__main__':
    app.run_server()
