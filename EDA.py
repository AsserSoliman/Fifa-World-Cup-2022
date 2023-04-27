import pandas as pd
import numpy as np 
import plotly.express as px 

def change_group(temp):
     G = ['A','B','C','D','E','F','G','H']
     return G[temp-1]
 
def load_data():
    df = pd.read_csv('group_stats.csv')
    df.group = df.group.apply(change_group)
    df = df.drop(columns=['Unnamed: 0'])
    return df
    
df = load_data()

def group_info_matches(Group):
    temp = df[df['group'] == Group]
    fig = px.bar(temp,x=temp.team,y=[temp.wins,temp.draws,temp.losses],barmode='group',labels={'value':"Matches",'team':'Team'},title=f"Matches info for every team in group {Group}")
    fig.update_yaxes(tickvals = [1,2,3])
    return fig 
    
def group_info_points(Group):
    temp = df[df['group'] == Group]
    fig = px.bar(temp,x=temp.team,y=temp.points,barmode='group',title=f"Matches info for every team in group {Group}")
    return fig

def groups_info_goals():
    temp = df.groupby('group')['goals_scored'].sum()
    fig = px.bar(x=temp.index,y=temp.values,barmode='group',labels={'x':"Groups",'y':'Goals'},title=f"Goals Scored in Each Group")
    return fig

def qualify(Group):
    temp = df[df['group'] == Group]
    return f"The 2 teams that qualified from group {Group} are {temp.team.iloc[0]} and {temp.team.iloc[1]} "