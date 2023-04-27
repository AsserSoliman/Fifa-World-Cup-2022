import pandas as pd
import plotly.express as px

def load_data():
    temp = pd.read_csv('team_data.csv')
    return temp 

df = load_data()

def show_unique():
    return tuple(df.team.unique())

def players(team):
    # l = []
    # for i in team.keys():
    #     l.append(i)
    temp = df[df['team'].isin(team)]
    z = temp.groupby('team').sum()
    
    fig = px.bar(z,x=z.index,y=['games','players_used','avg_age'],barmode='group')
    return fig 