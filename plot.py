import pandas as pd
import plotly
import plotly.graph_objs as go

#reading CSV file and parsing date
temp = pd.read_csv('Coal_Naturalgas_Generation_Data.csv',parse_dates=['Month'])

#preparing Data for Hover in Plotly
hovertexts0 = []
hovertexts1 = []
for indx in range(len(temp.Month)):
     hovertexts0.append('({y})Thousand MegaWattHours'.format(y=temp.natural_gas_thousand_megawatthours[indx]))
     hovertexts1.append('({y})Thousand MegaWattHours'.format(y=temp.coal_thousand_megawatthours[indx]))

#Plotting Lines for gas and coal seperately, and configuring hover text
trace0 = go.Scatter(x=temp.Month,y=temp.natural_gas_thousand_megawatthours,mode='lines',name='Natural gas',showlegend=True,hoverinfo='x+text',hovertext=hovertexts0)
trace1 = go.Scatter(x=temp.Month,y=temp.coal_thousand_megawatthours,mode='lines',name='Coal',hoverinfo='x+text',hovertext=hovertexts1)
data = [trace0,trace1]

#Adding title to the plot and axis
layout = go.Layout(title = "Coal and Natural Gas Electricity Generation", xaxis = dict(title='Year',tickmode = 'linear',tick0 = 'M1Y2005',dtick = 'M12'), yaxis = dict(title ='Thousand Megawatthours',tickformat=',d'),hovermode="closest")

#Plotting the plot offline and generating output file
plotly.offline.plot({"data":data,"layout":layout},filename='Coal_Naturalgas_Electricity_Generation.html',auto_open=True)