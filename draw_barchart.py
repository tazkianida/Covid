import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
import numpy as np
import seaborn as sns

df = pd.read_csv ('COVID19-20200917.csv')

df = pd.DataFrame(df.groupby(['country_name','date'])['cumulative_confirmed'].sum()).reset_index()

current_month = '2020-08-31'
dff = df[df['date'].eq(current_month)].sort_values(by='cumulative_confirmed', ascending=False).head(15)

fig, ax = plt.subplots(figsize=(15, 8))
sns.set(style="darkgrid")
ax.barh(dff['country_name'], dff['cumulative_confirmed'])

from datetime import datetime

fig, ax = plt.subplots(figsize=(15,8))
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

def draw_barchart(date):
    dff = df[df['date'].eq(date)].sort_values(by='cumulative_confirmed', ascending=True).tail(15)
    ax.clear()
    
    normal_colors = dict(zip(df['country_name'].unique(), rgb_colors_opacity))
    
    ax.barh(dff['country_name'], dff['cumulative_confirmed'], color = [normal_colors[x] for x in dff['country_name']])
    dx = dff['cumulative_confirmed'].max() / 100
    for i, (value, name) in enumerate(zip(dff['cumulative_confirmed'], dff['country_name'])):
        ax.text(value-dx, i, name, size=12, weight=800, ha='right')
        ax.text(value+dx, i, f'{value:,.0f}',  size=10, ha='left',  va='center')
        
    # Style the bar
    ax.text(1, 0.4, datetime.strptime(date, '%Y-%m-%d').strftime("%B"), transform=ax.transAxes, color='#766712', size=56, ha='right', weight=500)
    ax.text(1, 0.3, date, transform=ax.transAxes, color='#777777', size=20, ha='right', weight=500)
    ax.text(0, 1.06, 'Confirmed Cases', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, '\n\nCOVID-19 Confirmed Cases Worldwilde (Until August 2020)', transform=ax.transAxes, size=24, weight=600, ha='left')
    plt.box(False)
    plt.tight_layout()
    
draw_barchart('2020-08-31')
