import streamlit as st
from urllib.request import urlopen
from matplotlib import pyplot as plt
import json

with urlopen('https://raw.githubusercontent.com/faeldon/philippines-json-maps/master/geojson/provinces/hires/provinces-region-ph040000000.0.1.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("covid_region4a.csv")
import plotly.express as px

def render(Week = 0):
    data = {'ADM2_EN':  ['Batangas', 'Cavite', 'Laguna', 'Quezon', 'Rizal'],
        'cases': [
            df['Batangas'][Week],
            df['Cavite'][Week],
            df['Laguna'][Week],
            df['Quezon'][Week],
            df['Rizal'][Week]
            ],
            }    

    fig = px.choropleth_mapbox(data, geojson=counties, featureidkey="properties.ADM2_EN",
                            locations='ADM2_EN', color='cases',
                               color_continuous_scale="YlOrRd",
                               mapbox_style="carto-positron",
                               labels={'cases':'Number of Cases'},
                               zoom = 7,
                               center = {"lat": 14.249701614019127, "lon":  121.18649902198216},
                              )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, title = "Plot Title")
    fig.update_geos(fitbounds="locations")
    return fig

Week = st.slider('Week', 0, 114, 1)
st.write("Dates : ", df['Dates'][Week])
st.plotly_chart(render(Week))
