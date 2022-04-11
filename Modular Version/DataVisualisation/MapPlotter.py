mport numpy as np
import plotly.offline as offline
from sklearn.preprocessing import MinMaxScaler
import plotly
import plotly.figure_factory as ff
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
import pandas as pd
scaler = MinMaxScaler((0,100))

import plotly.express as px
for i in range(1,10):
  df =  pd.read_csv('https://raw.githubusercontent.com/SparshRastogi/Covid-19-Risk-Calculator/main/2021%20Month' + str(i) + '%20Risk.csv')
  df['FIPS CODE']=df['FIPS CODE'].apply(lambda x: '{0:0>5}'.format(x) )
  df['risk'] = scaler.fit_transform(np.array(df['risk']).reshape(-1,1))
  fig = px.choropleth(df,geojson = counties,locations='FIPS CODE', color='risk',
                           color_continuous_scale="ylorrd",
                           range_color=(df['risk'].min(),df['risk'].max()),
                           scope="usa")
  fig.show()
