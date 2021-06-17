import pandas as pd
import plotly.express as px

input = input("What Bar Do You Want To Look At For Covid's Data, b for Bar Graph, l for Line Graph and s for Scatter Graph")

if input == 'b':
    df = pd.read_csv('data.csv')
    fig = px.bar(df,x = 'Country', y = 'InternetUsers')
    fig.show()
elif input == 'l':
    df = pd.read_csv('data.csv')
    fig = px.line(df,x = 'Country', y = 'InternetUsers')
    fig.show()
elif input == 's':
    df = pd.read_csv('data.csv')
    fig = px.bar(df,x = 'Country', y = 'InternetUsers')
    fig.show()