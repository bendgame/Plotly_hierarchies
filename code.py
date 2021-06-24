import plotly.express as px
import pandas as pd

df = pd.read_excel('sp500.xlsx')

df['constant'] = 1

df.head()

fig =px.sunburst(
    df,
    path = ['GICS\xa0Sector', 'GICS Sub-Industry', 'Symbol'],
    values = df['constant']
)
fig.show()

fig =px.treemap(
    df,
    path = ['GICS\xa0Sector', 'GICS Sub-Industry', 'Symbol'],
    values = df['constant'],
    color='GICS Sub-Industry', 
    hover_data=['Security'],
    color_continuous_scale='RdBu'
)
#fig.update_traces(root_color="lightgrey")
fig.show()


fig =px.icicle(
    df,
    path = [px.Constant("SP500"),'GICS\xa0Sector', 'GICS Sub-Industry', 'Symbol'],
    values = df['constant'],
    hover_data=['Security'],
    color_continuous_scale='RdBu'
)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()

