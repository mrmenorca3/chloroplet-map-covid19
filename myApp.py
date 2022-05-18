import streamlit as st
import numpy as np
from urllib.request import urlopen
from ipywidgets import interact
from matplotlib import pyplot as plt
import json

with urlopen('https://raw.githubusercontent.com/faeldon/philippines-json-maps/master/geojson/provinces/hires/provinces-region-ph040000000.0.1.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("covid_region4a.csv")
import plotly.express as px

st.header('This is the Title')
st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

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

    fig = px.choropleth(data, geojson=counties, featureidkey="properties.ADM2_EN",
                            locations='ADM2_EN', color='cases',
                               color_continuous_scale="Reds",
                               labels={'cases':'Number of Cases'},
                              )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, title = "Plot Title")
    fig.update_geos(fitbounds="locations")
    return fig

Week = st.slider('Week', 0, 114, 1)
st.plotly_chart(render(Week))

